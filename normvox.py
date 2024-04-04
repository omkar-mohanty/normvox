import voxlib.voxelize

def normvox(filename, dim):
    out = voxlib.voxelize.voxelize(filename, dim)
    matrix = (dim, dim , dim)
    matrix = [[[0.0 for _ in range(matrix_size[2])] for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]

    for coord in coordinates:

    x, y, z = coord
    x += dim - 1  
    y += dim - 1  
    z += dim - 1  

    matrix[x][y][z] = 1.0
    return matrix
