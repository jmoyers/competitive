import json
import os

print(os.getcwd())

problem_json_file = os.path.join(os.getcwd(), "leetcode", "problems.json")

with open(problem_json_file) as json_file:
    data = json.load(json_file)

    data = data["stat_status_pairs"]

    for problem in data:
        num = problem["stat"]["question_id"]
        title = problem["stat"]["question__title"]
        slug = problem["stat"]["question__title_slug"]
        url = f"https://leetcode.com/problems/{slug}"
        level = problem["difficulty"]["level"]

        difficulty = ""

        if level == 1:
            difficulty = "easy"
        elif level == 2:
            difficulty = "medium"
        elif level == 3:
            difficulty = "hard"

        filename = os.path.join(os.getcwd(), "leetcode", f"{num}.py")

        if os.path.isfile(filename):
            with open(filename, "r+") as problem_file:
                contents = problem_file.readlines()

                # check if front matter exists
                start = False
                end = False

                for line in contents:
                    if start and not end and "---" in line:
                        end = True
                    if not start and "---" in line:
                        start = True
                    if start and end:
                        break

                first = True

                for i, line in enumerate(contents):
                    if "---" in line and len(line.strip()) > 3:
                        contents[i] = line[:3] + "\n" + line[3:]
                    else:
                        break

                for i, line in enumerate(contents):
                    if '"""' in line:
                        break
                    if line[0] == "#":
                        if first:
                            contents.insert(i, '"""')
                            first = False
                        else:
                            if line[1] == " ":
                                contents[i] = line[2:]
                            else:
                                contents[i] = line[1:]
                    else:
                        contents.insert(i, '"""')
                        break

                if not (start and end):
                    fm = [
                        "---\n",
                        f"title: {title}\n",
                        f"difficulty: {difficulty}\n",
                        f"level: {level}\n",
                        f"links: \n",
                        f"- {url}\n",
                        "---\n",
                    ]

                    contents = contents[0:1] + fm + contents[1:]

                problem_file.seek(0)
                problem_file.write("".join(contents))
                problem_file.truncate()

