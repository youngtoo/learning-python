# Lets do a collection
test_scores = {
    'Ian': 30,
    'Partrick' : 78,
    'Loreen' : 99,
    'Bernard' : 63
}

# Loop through a copy of the test scores
for student, score in test_scores.copy().items():
    print( student, " scored " , score, end='\n')

# Loop through something
for i in range(10, 100, 15):
    print(i + 1, ". I will never give up again.")

# Combine range and length