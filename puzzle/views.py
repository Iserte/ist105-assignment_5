from django.shortcuts import render
from .forms import PuzzleForm
import math
import random

def puzzle_view(request):
    result = None

    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']

            # Number Puzzle
            if number % 2 == 0:
                number_type = 'even'
                number_result = f'Square root: {math.sqrt(number):.2f}'
            else:
                number_type = 'odd'
                number_result = f'Cube: {number ** 3}'

            # Text Puzzle
            binary_text = ' '.join(format(ord(char), '08b') for char in text)
            vowels = 'aeiouAEIOU'
            vowel_count = sum(1 for char in text if char in vowels)

            # Treasure Hunt
            secret = random.randint(1, 100)
            attempts = []
            for i in range(1, 6):
                guess = random.randint(1, 100)
                if guess == secret:
                    attempts.append(f'Attempt {i}: {guess} (Correct!)')
                    win = True
                    break
                elif guess < secret:
                    attempts.append(f'Attempt {i}: {guess} (Too low!)')
                else:
                    attempts.append(f'Attempt {i}: {guess} (Too high!)')
            else:
                win = False
                attempts.append(f'Failed to find the treasure in 5 attempts.')

            result = {
                'number': number,
                'number_type': number_type,
                'number_result': number_result,
                'text': text,
                'binary_text': binary_text,
                'vowel_count': vowel_count,
                'secret': secret,
                'attempts': attempts,
                'win': win
            }
    else:
        form = PuzzleForm()

    return render(request, 'puzzle/puzzle.html', {'form': form, 'result': result})