#include <iostream>
#include <cstdlib> // Для использования функции exit()

class Matrix {
private:
    float** elements;
    int rows;
    int cols;
    int errorCode; // Код ошибки

public:
    // Конструкторы
    Matrix() {
        rows = 1;
        cols = 1;
        elements = new float*[rows];
        elements[0] = new float[cols];
        if (elements == nullptr || elements[0] == nullptr) {
            errorCode = 1; // Ошибка выделения памяти
            exit(1);
        }
        elements[0][0] = 0.0f; // Инициализация элемента
    }

    Matrix(int r, int c) {
        rows = r;
        cols = c;
        elements = new float*[rows];
        for (int i = 0; i < rows; ++i) {
            elements[i] = new float[cols];
            if (elements[i] == nullptr) {
                errorCode = 1; // Ошибка выделения памяти
                exit(1);
            }
            for (int j = 0; j < cols; ++j) {
                elements[i][j] = 0.0f; // Инициализация всех элементов нулями
            }
        }
    }

    // Деструктор
    ~Matrix() {
        for (int i = 0; i < rows; ++i) {
            delete[] elements[i];
        }
        delete[] elements;
    }

    // Метод доступа к элементу (i, j)
    float getElement(int i, int j) {
        if (i >= 0 && i < rows && j >= 0 && j < cols) {
            return elements[i][j];
        } else {
            errorCode = 2; // Выход за пределы массива
            return 0.0f;
        }
    }

    // Метод доступа к адресу элемента (i, j)
    float* getElementAddress(int i, int j) {
        if (i >= 0 && i < rows && j >= 0 && j < cols) {
            return &elements[i][j];
        } else {
            errorCode = 2; // Выход за пределы массива
            return nullptr;
        }
    }

    // Функция печати
    void print() {
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                std::cout << elements[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    // Функции арифметических операций

    // Сложение матрицы с матрицей
    Matrix operator+(const Matrix& other) {
        if (rows != other.rows || cols != other.cols) {
            errorCode = 3; // Несоответствие размерностей
            exit(1);
        }
        Matrix result(rows, cols);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                result.elements[i][j] = elements[i][j] + other.elements[i][j];
            }
        }
        return result;
    }

    // Вычитание матрицы из матрицы
    Matrix operator-(const Matrix& other) {
        if (rows != other.rows || cols != other.cols) {
            errorCode = 3; // Несоответствие размерностей
            exit(1);
        }
        Matrix result(rows, cols);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                result.elements[i][j] = elements[i][j] - other.elements[i][j];
            }
        }
        return result;
    }

    // Умножение матрицы на матрицу
    Matrix operator*(const Matrix& other) {
        if (cols != other.rows) {
            errorCode = 3; // Несоответствие размерностей
            exit(1);
        }
        Matrix result(rows, other.cols);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < other.cols; ++j) {
                for (int k = 0; k < cols; ++k) {
                    result.elements[i][j] += elements[i][k] * other.elements[k][j];
                }
            }
        }
        return result;
    }

    // Умножение матрицы на число
    Matrix operator*(float scalar) {
        Matrix result(rows, cols);
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                result.elements[i][j] = elements[i][j] * scalar;
            }
        }
        return result;
    }
};

int main() {
    Matrix m1; // Конструктор без параметров
    Matrix m2(2, 2); // Конструктор с двумя параметрами
    Matrix m3(2, 3); // Конструктор с двумя параметрами

    // Пример использования методов
    m1.print();
    std::cout << std::endl;
    m2.print();
    std::cout << std::endl;
    m3.print();

    return 0;
}
