#!/opt/miniconda/python 
import sys
import random 

# Database
quotes = '''
1. "Be the change that you wish to see in the world." - Mahatma Gandhi
2. "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment." - Ralph Waldo Emerson
3. "The only thing necessary for the triumph of evil is for good men to do nothing." - Edmund Burke
4. "The only true wisdom is in knowing you know nothing." - Socrates
5. "In three words I can sum up everything I've learned about life: It goes on." - Robert Frost
6. "Life is what happens when you're busy making other plans." - John Lennon
7. "The only limit to our realization of tomorrow will be our doubts of today." - Franklin D. Roosevelt
8. "The greatest glory in living lies not in never falling, but in rising every time we fall." - Nelson Mandela
9. "I have not failed. I've just found 10,000 ways that won't work." - Thomas A. Edison
10. "Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that." - Martin Luther King Jr.
11. "It is during our darkest moments that we must focus to see the light." - Aristotle Onassis
12. "Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill
13. "The future belongs to those who believe in the beauty of their dreams." - Eleanor Roosevelt
14. "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe." - Albert Einstein
15. "The best way to predict the future is to create it." - Peter Drucker
16. "A journey of a thousand miles begins with a single step." - Lao Tzu
17. "Life isn't about finding yourself. Life is about creating yourself." - George Bernard Shaw
18. "Success is stumbling from failure to failure with no loss of enthusiasm." - Winston Churchill
19. "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it." - Jordan Belfort
20. "If you want to lift yourself up, lift up someone else." - Booker T. Washington
21. "The only constant in life is change." - Heraclitus
22. "The journey of a thousand miles begins with a single step." - Lao Tzu
23. "The mind is everything. What you think you become." - Buddha
24. "Our greatest glory is not in never falling, but in rising every time we fall." - Confucius
25. "Don't cry because it's over, smile because it happened." - Dr. Seuss
26. "No one can make you feel inferior without your consent." - Eleanor Roosevelt
27. "The unexamined life is not worth living." - Socrates
28. "Believe you can and you're halfway there." - Theodore Roosevelt
29. "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment." - Ralph Waldo Emerson
30. "Happiness is not something readymade. It comes from your own actions." - Dalai Lama
31. "Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution." - Albert Einstein
32. "It does not matter how slowly you go as long as you do not stop." - Confucius
33. "The only way to do great work is to love what you do." - Steve Jobs
34. "We can't help everyone, but everyone can help someone." - Ronald Reagan
35. "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it." - Jordan Belfort
36. "Education is the most powerful weapon which you can use to change the world." - Nelson Mandela
37. "The only true wisdom is in knowing you know nothing." - Socrates
38. "The best way to predict the future is to create it." - Peter Drucker
39. "The only limit to our realization of tomorrow will be our doubts of today." - Franklin D. Roosevelt
40. "If you want to lift yourself up, lift up someone else." - Booker T. Washington
41. "I have not failed. I've just found 10,000 ways that won't work." - Thomas A. Edison
42. "If you want to achieve greatness, stop asking for permission." - Anonymous
43. "What lies behind us and what lies before us are tiny matters compared to what lies within us." - Ralph Waldo Emerson
44. "You miss 100% of the shots you don't take." - Wayne Gretzky
45. "Life is 10% what happens to us and 90% how we react to it." - Charles R. Swindoll
46. "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment." - Buddha
47. "The best time to plant a tree was 20 years ago. The second best time is now." - Chinese Proverb
48. "The only way to do great work is to love what you do." - Steve Jobs
49. "Don't judge each day by the harvest you reap but by the seeds that you plant." - Robert Louis Stevenson
50. "A person who never made a mistake never tried anything new." - Albert Einstein
51. "The future belongs to those who believe in the beauty of their dreams." - Eleanor Roosevelt
52. "If you're going through hell, keep going." - Winston Churchill
53. "In the end, we will remember not the words of our enemies, but the silence of our friends." - Martin Luther King Jr.
54. "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light." - Plato
55. "Every strike brings me closer to the next home run." - Babe Ruth
56. "The only thing we have to fear is fear itself." - Franklin D. Roosevelt
57. "What lies behind us and what lies before us are tiny matters compared to what lies within us." - Ralph Waldo Emerson
58. "A ship in harbor is safe, but that is not what ships are built for." - John A. Shedd
59. "The two most important days in your life are the day you are born and the day you find out why." - Mark Twain
60. "Your time is limited, don't waste it living someone else's life." - Steve Jobs
61. "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it." - Jordan Belfort
62'''

# break a string into lines
quote_array=[]
for line in quotes.split('\n'):
    quote_array.append(line)
  
size = len(quote_array) 
val = 'y'
while ( val != 'n' ):
  ran_quote = random.randint(0, size-1)
  print("=====\n", quote_array[ran_quote], "\n=======\n")
  val = input("Want another?")