"""
---
title: Strong Password Checker
difficulty: hard
level: 3
tags:
- password
- minimum change
- novel algorithm
links: 
- https://leetcode.com/problems/strong-password-checker
- https://leetcode.com/problems/strong-password-checker/discuss/91008/Simple-Python-solution
---
A password is considered strong if below conditions are all met:

    It has at least 6 characters and at most 20 characters.

    It must contain at least one lowercase letter, at least one uppercase
    letter, and at least one digit.

    It must NOT contain three repeating characters in a row ("...aaa..." is
    weak, but "...aa...a..." is strong, assuming other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input,
and return the MINIMUM change required to make s a strong password. If s is
already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one
change.
"""

from random import sample


class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        # we don't even need to know which types are missing, just the total
        # number that are missing
        missing_type = 3

        # check for each of the three requirements
        if any("a" <= c <= "z" for c in s):
            missing_type -= 1
        if any("A" <= c <= "Z" for c in s):
            missing_type -= 1
        if any(c.isdigit() for c in s):
            missing_type -= 1

        # the only tricky bit. determine streaks and collapse their mitigation
        # strategy with insertion/deletion requirement. insertion is also easy,
        # because we can convince ourselves that breaking streaks doesn't matter
        # in the < 6 case. i'll show that below in coments.

        # we need a minimum of 1 change per repeating 3 characters
        # the change can be replace, delete, insert

        # in the case where 6 <= len <= 20, this can be a replacement and there
        # is no overlap

        # in the case where its larger, we do need to collapse our replacement
        # and deletion requirements, and we do that with some modulo math to
        # cover 3 cases

        # minimally we need streak_length / 3 changes to get rid of the streak,
        # some of which can be deletions, if we have a string that is too long

        # % 3 == 0 - aaa, aaaaaa - here we can delete one character to break
        # one streak. minimally we need streak / 3 changes. we can reduce the
        # number of needed replaces by one by deleting one character

        # to convince ourselves, aaa -> aa

        # % 3 == 1 - aaaa, aaaaaaa - here we can delete two characters to create
        # a % 3 == 2 situation if the streak was longer than triplet

        # to convince ourselves, aaaa -> aa

        # % 3 == 2 - aaaaa - the "base case," whereby if you delete 3 characters
        # you subtract 1 sequence

        # to convince ourselves, aaaaa -> aa
        change = one = two = 0

        # we start at i = 2 because we're looking for streaks of three,
        # simplifies conditional

        i = 2

        while i < len(s):
            if s[i] == s[i - 1] == s[i - 2]:
                # streak of 3 exists, we immediately set streak length to
                # 3 in the below first iteration
                length = 2

                # detect if the streak goes further than just 3 characters
                # first iteration is redundant with the above conditional
                while i < len(s) and s[i] == s[i - 1]:
                    length += 1
                    i += 1

                # our streak length is accurate even for longer-than-3 streaks

                # minimum number of changes required, we'll collapse this with
                # deletions below
                change += length // 3

                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                i += 1

        # we've processed all the repeating character sequences
        # now we can deal with the 3 cases

        # we need to insert as many as possible for total required
        # changes. we're only concerned with the missing categorical
        # requirements in upper/lower/digits

        # we aren't concerned about < 6 repeating characters because they are
        # naturall resolved by the insertion and unique character budgets

        # Lets take a look at two examples to convince ourselves this is true.

        # aaaaa
        # aaAaa3 - one insertion, one replacement, both in the budget for
        # uppercase and digit count respectively

        # aaaB3
        # aaiaB3 - one insertion, but its covered by the budget associated with
        # the length requirement (one addition, in this case it overlaps with
        # breaking up the repeated character)

        # this should whole true for all strings below 6 characters
        if len(s) < 6:
            # streak breaking overlaps entirely with adding characters
            return max(missing_type, 6 - len(s))
        elif len(s) <= 20:
            # streaking overlaps entirely with replacement
            return max(missing_type, change)
        else:
            # streak breaking can only be proved to partially overlap with
            # deleting characters

            # total deletion budget, this has to be satisfied
            delete = len(s) - 20

            budget = delete

            # we need to collapse streak breaking budget with deletion

            # every time we encountered aaa -> aa (1 x deletes)
            change -= min(budget, one)

            # reduce delete budget for triplets encounterd
            budget = max(budget - one, 0)

            # every time we encountered aaaa -> aa (2 x deletes)
            change -= min(budget, two * 2) // 2

            # reduce budget again based on quadruplets encountered
            budget = max(budget - 2 * two, 0)

            # every time we encountered aaaaa -> aa (3 x deletes)
            change -= budget // 3

            # we needed MINIMALLY to delete `delete` characters, we were simply
            # reducing the replace budget of changes required to break streaks
            # found. streak breaking also overlap with replacements to add
            # missing types
            return delete + max(missing_type, change)


def test_password_checker():
    print(Solution().strongPasswordChecker("1Abababcaaaabababababa"))
