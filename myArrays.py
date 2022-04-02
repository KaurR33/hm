
import numpy as np
def main():


    r = int(input("Number of reviewers:"))

    m = int(input("Number of movies:"))

    # Define the matrix

    matrix = []

    print("Enter the entries row-wise:")

    # for user input

    for i in range(r):  # A for loop for row entries

        a = []

        for j in range(m):  # A for loop for column entries

            a.append(int(input()))

        matrix.append(a)

    # To print the matrix

    def displayArray():
        for i in range(r):

            for j in range(m):
                print(matrix[i][j], end=" ")

            print()
    displayArray()

    #Lowest & Higest rating
    def printHighestLowestMovieRating():
        arr1 = np.matrix

        print(f'Original Array:\n{arr1}')

        arr1_transpose = arr1.transpose()

        print(f'Transposed Array:\n{arr1_transpose}')
    printHighestLowestMovieRating()

main()
