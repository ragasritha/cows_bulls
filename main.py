#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
def random_number():
    while True:
        n = str(randint(100, 999))
        if not (n[0] == n[1] or n[1] == n[2] or n[0] == n[2]):
            return n
name = input("Welcome to the Cows and Bulls game! Please enter your name: ")
print("hi", name)
chances = 5
cows = 0
bulls = 0
num = str(random_number())
while chances > 0:
    print("You have", chances, "chances left!")
    guess = str(input("Enter your guess: "))
    if num == guess:
        print("Great! You got it right.")
        break
    else:
        guessed_digits = set()
        for i in range(0, 3):
            if guess[i] == num[i]:
                bulls += 1
            elif guess[i] in num and guess[i] not in guessed_digits:
                cows += 1
                guessed_digits.add(guess[i])
        print("Keep going. You have", bulls, "bulls and", cows, "cows.")
        bulls = 0
        cows = 0
        chances -= 1
print("The correct answer is", num)


# In[ ]:




