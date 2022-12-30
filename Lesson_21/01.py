class Matrix:
    def __init__(self, m_list):
        for i in range(len(m_list)-1):
            if len(m_list[i]) != len(m_list[i+1]):
                raise Exception (f"Can't create matrix from {m_list} list")
        self.matrix = m_list
        self.n_col = len(m_list)
        self.n_row = len(m_list[0])

    def m_print(self):
        print('Result matrix:')
        [print(i) for i in self.matrix]


    def as_matrix(self, n_row, n_col):
        if self.n_row < n_col:
            for row in self.matrix:
                row.extend([0] * (n_col - self.n_row))
            self.n_row = n_col
        if self.n_col < n_row:
            self.matrix.extend([[0] * self.n_row] * (n_row - self.n_row))

    def v_mult(self, var):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] * var)
        return Matrix(result)

    def m_sum(self, data):
        m = max(self.n_col, data.n_col)
        n = max(self.n_row, data.n_row)
        self.as_matrix(m, n)
        data.as_matrix(m, n)
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] + data.matrix[i][j])
        return Matrix(result)


    def m_sub(self, data):
        m = max(self.n_col, data.n_col)
        n = max(self.n_row, data.n_row)
        self.as_matrix(m, n)
        data.as_matrix(m, n)
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                result[i].append(self.matrix[i][j] - data.matrix[i][j])
        return Matrix(result)


    def m_transpose(self):
        result = [[0] * len(self.matrix) for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result[j][i] = self.matrix[i][j]
        return Matrix(result)


    def m_mult(self, data):
        if self.n_row != data.n_col:
            raise Exception(f'Number of row({self.n_row}) != number of col({data.n_col})')
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(data.matrix[i])):
                m_sum = 0
                for k in range(len(data.matrix)):
                    m_sum += self.matrix[i][k] * data.matrix[k][j]
                result[i].append(m_sum)
        return Matrix(result)


A = Matrix(m_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = Matrix(m_list = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

A.m_print()
C = A.m_sum(B)
C.m_print()

C = A.v_mult(2)
C.m_print()

C = A.m_sub(B)
C.m_print()

C = A.m_mult(B)
C.m_print()

C = A.m_transpose()
C.m_print()

D = Matrix(m_list= [
    [1, 2]
])
C = A.m_mult(D)
C.m_print()
