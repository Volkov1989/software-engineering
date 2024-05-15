#include iostream
#include cstdlib  Для использования функции exit()

class Vector {
private
    float elements;
    int size;
    int errorCode;  Код ошибки

public
    static int count;  Статическая переменная для подсчета числа объектов

     Конструкторы
    Vector() {
        size = 1;
        elements = new float[size];
        if (elements == nullptr) {
            errorCode = 1;  Ошибка выделения памяти
            exit(1);
        }
        elements[0] = 0.0f;  Инициализация первого элемента
        count++;
    }

    Vector(int s) {
        size = s;
        elements = new float[size];
        if (elements == nullptr) {
            errorCode = 1;  Ошибка выделения памяти
            exit(1);
        }
        for (int i = 0; i  size; ++i) {
            elements[i] = i;  Инициализация элементов от 0 до size-1
        }
        count++;
    }

    Vector(int s, float val) {
        size = s;
        elements = new float[size];
        if (elements == nullptr) {
            errorCode = 1;  Ошибка выделения памяти
            exit(1);
        }
        for (int i = 0; i  size; ++i) {
            elements[i] = val;  Инициализация всех элементов значением val
        }
        count++;
    }

     Деструктор
    ~Vector() {
        delete[] elements;
        count--;
    }

     Функция присваивания значения элементу массива
    void setElement(int index, float value = 0.0f) {
        if (index = 0 && index  size) {
            elements[index] = value;
        } else {
            errorCode = 2;  Выход за пределы массива
        }
    }

     Функция получения значения элемента массива
    float getElement(int index) {
        if (index = 0 && index  size) {
            return elements[index];
        } else {
            errorCode = 2;  Выход за пределы массива
            return 0.0f;
        }
    }

     Функция печати
    void print() {
        for (int i = 0; i  size; ++i) {
            stdcout  elements[i]   ;
        }
        stdcout  stdendl;
    }

     Функции арифметических операций
    Vector operator+(const Vector& other) {
        Vector result(size);
        for (int i = 0; i  size; ++i) {
            result.elements[i] = elements[i] + other.elements[i];
        }
        return result;
    }

    Vector operator(float scalar) {
        Vector result(size);
        for (int i = 0; i  size; ++i) {
            result.elements[i] = elements[i]  scalar;
        }
        return result;
    }

    Vector operator-(const Vector& other) {
        Vector result(size);
        for (int i = 0; i  size; ++i) {
            result.elements[i] = elements[i] - other.elements[i];
        }
        return result;
    }

     Методы сравнения
    bool operator(const Vector& other) {
        float sum1 = 0.0f, sum2 = 0.0f;
        for (int i = 0; i  size; ++i) {
            sum1 += elements[i];
            sum2 += other.elements[i];
        }
        return sum1  sum2;
    }

    bool operator(const Vector& other) {
        float sum1 = 0.0f, sum2 = 0.0f;
        for (int i = 0; i  size; ++i) {
            sum1 += elements[i];
            sum2 += other.elements[i];
        }
        return sum1  sum2;
    }

    bool operator==(const Vector& other) {
        float sum1 = 0.0f, sum2 = 0.0f;
        for (int i = 0; i  size; ++i) {
            sum1 += elements[i];
            sum2 += other.elements[i];
        }
        return sum1 == sum2;
    }
};

 Инициализация статической переменной
int Vectorcount = 0;

int main() {
    Vector v1;  Конструктор без параметров
    Vector v2(5);  Конструктор с одним параметром
    Vector v3(3, 2.5f);  Конструктор с двумя параметрами

     Пример использования методов
    v1.print();
    v2.print();
    v3.print();

    return 0;
}
