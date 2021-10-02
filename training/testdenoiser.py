import main_test_dncnn

# Test prior trained on 9.75% noise on training image with 9.75% added noise
main_test_dncnn.main()
# Test prior trained on 2% noise on training image with 2% added noise
main_test_dncnn.main(2, 2)
# Test prior trained on 5% noise on training image with 5% added noise
#main_test_dncnn.main(5, 5)