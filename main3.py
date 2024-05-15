#include <iostream>
#include <cstdlib> // Для использования функции exit()

class TicTacToe {
private:
    char board[3][3]; // Поле для игры

public:
    // Конструктор
    TicTacToe() {
        // Инициализация поля пустыми клетками
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                board[i][j] = '-';
            }
        }
    }

    // Функция для вывода текущего состояния игрового поля
    void printBoard() {
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                std::cout << board[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    // Функция для хода игрока
    bool makeMove(int row, int col, char player) {
        if (row >= 0 && row < 3 && col >= 0 && col < 3 && board[row][col] == '-') {
            board[row][col] = player;
            return true;
        } else {
            return false; // Ход невозможен
        }
    }
};

int main() {
    TicTacToe game;

    // Пример хода игрока
    game.makeMove(0, 0, 'X');
    game.makeMove(1, 1, 'O');

    // Вывод текущего состояния поля
    game.printBoard();

    return 0;
}
