class GuessNumber(object):
    def __init__(self, number, min, max):
        self.guesses = 0
        self.number = number
        self.min = min
        self.max = max

    def get_guess(self):
        guess = input(f"Please guess a Number ({self.min} - {self.max}): ")
        if self.valid_number(guess):
            return int(guess)
        else:
            print("Enter a valid Number")
            return self.get_guess()

    def valid_number(self, number):
        try:
            number = int(number)
        except:
            return False
        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1
            
            guess = self.get_guess()

            if guess < self.number:
                print("Your guess is low")
            elif guess > self.number:
                print("Your guess was high")
            else:
                break

        print(f"You guessed exact Number in {self.guesses} guesses.")


game = GuessNumber(45, 0, 100)
game.play()