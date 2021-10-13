import main_test_dncnn

#Experiment: test denoisers trained for various durations

# Test prior trained on 9.75% noise on training image with 9.75% added noise (trained for 1000 iterations)
main_test_dncnn.main(9.75, 9.75, 1000)
# Test prior trained on 9.75% noise on training image with 9.75% added noise (trained for 24 hours)
main_test_dncnn.main(9.75, 9.75, 5000)
# Test prior trained on 9.75% noise on training image with 9.75% added noise (trained for 24 hours)
main_test_dncnn.main(9.75, 9.75, 10000)

#Experiment: test denoisers trained for on various noise levels

# Test prior trained on 9.75% noise on training image with 9.75% added noise (trained for 1000 iterations)
main_test_dncnn.main(9.75, 9.75, 1000)
# Test prior trained on 5% noise on training image with 9.75% added noise (trained for 1000 iterations)
main_test_dncnn.main(5, 9.75, 1000)
# Test prior trained on 2% noise on training image with 9.75% added noise (trained for 1000 iterations)
main_test_dncnn.main(2, 9.75, 1000)

# Test prior trained on 9.75% noise on training image with 5% added noise (trained for 1000 iterations)
main_test_dncnn.main(9.75, 5, 1000)
# Test prior trained on 5% noise on training image with 5% added noise (trained for 1000 iterations)
main_test_dncnn.main(5, 5, 1000)
# Test prior trained on 2% noise on training image with 5% added noise (trained for 1000 iterations)
main_test_dncnn.main(2, 5, 1000)

# Test prior trained on 9.75% noise on training image with 2% added noise (trained for 1000 iterations)
main_test_dncnn.main(9.75, 2, 1000)
# Test prior trained on 5% noise on training image with 2% added noise (trained for 1000 iterations)
main_test_dncnn.main(5, 2, 1000)
# Test prior trained on 2% noise on training image with 2% added noise (trained for 1000 iterations)
main_test_dncnn.main(2, 2, 1000)
