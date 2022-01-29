class Solution {
public:
  vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
    // matrix multiplication is entry by entry multiplication where first row is multiplied
    // by first column, and so on
    
    // we do need to assume a's columns = b's columns, so we don't have to check that part of
    // input for validity
    
    // are there other cases where input is malformed?  todo
    
    // resulting matrix is A rows x B cols large
    
    vector<vector<int>> R(A.size(), vector<int>(B[0].size()));
    
    // 1 row in A
    // all cols in B
    
    for (int i = 0; i < A.size(); i++){      
      // calc dot product
      for (int j = 0; j < B[0].size(); j++) {        
        int sum = 0;
        for (int k = 0; k < B.size(); k++) {          
          //cout << A[i][k] << " * " << B[k][j] << endl;
          sum += (A[i][k] * B[k][j]);
        }
        //cout << "as " << sum << " " << i << ", " << j << endl;
        R[i][j] = sum;
        //cout << "done" << endl;
      }  
    }
    
    return R;
  }
};
