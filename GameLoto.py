import random


class LottoCard:

    ROWS_NUMBER = 3
    SPACES_IN_ROWS = 3
    CELLS_IN_ROW = 9

    def get_three_random_position(self):
        poses = set()
        while len(poses) != self.ROWS_NUMBER:
            poses.add(random.randrange(0, self.CELLS_IN_ROW, 1))
        return poses

    def __init__(self):
        self.number_arr = []
        numbers = set()
        while len(numbers) != (self.CELLS_IN_ROW - self.SPACES_IN_ROWS) * self.ROWS_NUMBER:
            numbers.add(random.randrange(1, 90, 1))
        for k in range(self.ROWS_NUMBER):
            j = 0
            result = []
            poses = self.get_three_random_position()
            arr = list(numbers)[(self.CELLS_IN_ROW - self.SPACES_IN_ROWS) * k:(self.CELLS_IN_ROW - self.SPACES_IN_ROWS) * k + (self.CELLS_IN_ROW - self.SPACES_IN_ROWS)]
            arr.sort()
            for i in range(self.CELLS_IN_ROW):
                if i not in poses:
                    result.append(arr[j])
                    j += 1
                else:
                    result.append(" ")
            self.number_arr.append(result)

    def __str__(self):
        result = ""
        for i in range(self.ROWS_NUMBER):
            result += "| "
            for j in range(9):
                result += str(self.number_arr[i][j]).rjust(2) + " "
            result += "|\n"
        return result


class LottoGame:

    def element_in_massive(self, array):
        try:
            return array.index(self.selected_number)
        except ValueError:
            return -1

    def __init__(self):
        self.user_card = LottoCard()
        self.computer_card = LottoCard()
        self.numbers = [i for i in range(1, 90)]
        self.is_over = False
        self.selected_number = 0

    def contains(self, some_card):
        return (self.selected_number in some_card.number_arr[0]) | (self.selected_number in some_card.number_arr[1]) | (self.selected_number in some_card.number_arr[2])

    def del_number(self, some_card):
        for i in range(some_card.ROWS_NUMBER):
            if self.selected_number in some_card.number_arr[i]:
                some_card.number_arr[i] = [el if el != self.selected_number else " " for el in some_card.number_arr[i]]
                break

    @staticmethod
    def card_empty(card):
        for i in range(card.ROWS_NUMBER):
            for j in range(card.CELLS_IN_ROW):
                if card.number_arr[i][j] != " ":
                    return False
        return True

    def start(self):
        winner = ''
        while not self.is_over:
            print(self.user_card)
            print(self.computer_card)
            self.selected_number = random.randrange(1, len(self.numbers))
            print(f"Do you have {self.selected_number}\n yes or no?")
            answer = input("Something\n")
            user_result = self.contains(self.user_card)
            if user_result:
                self.del_number(self.user_card)
            if self.contains(self.computer_card):
                self.del_number(self.computer_card)
            self.is_over = (user_result & (answer == "no")) | ((not user_result) & (answer == "yes"))
            if self.is_over:
                winner = "Computer"
                break
            self.is_over = self.card_empty(self.user_card)
            if self.is_over:
                winner = "You"
                break
            self.is_over = self.card_empty(self.computer_card)
            if self.is_over:
                winner = "Computer"
                break
        print(f"Game is over. {winner} win{'s' if winner == 'Computer' else ''}!")


LottoGame().start()
