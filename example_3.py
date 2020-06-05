# def wrapper_function():
#     something = 10
#
#     def inner():
#         print(something)
#
#     print(something)
#     inner()
#     print(something)
#
# wrapper_function()

#
#
# def wrapper_function():
#     something = 10
#
#     def inner():
#         something = 8
#         print(something)
#
#     print(something)
#     inner()
#     print(something)
#
# wrapper_function()
#
#
# def wrapper_function():
#     something = 10
#
#     def inner():
#         nonlocal something
#         something = 8
#         print(something)
#
#     print(something)
#     inner()
#     print(something)
#
# wrapper_function()
#
#
# def most_external():
#     value = 5
#
#     def inner():
#         print(value)
#
#         def even_deeper():
#             print(value)
#
#         even_deeper()
#
#     print(value)
#     inner()
#     print(value)
#
#
# most_external()

#
# def most_external():
#     value = 5
#
#     def inner():
#         value = 88
#         print(value)
#
#         def even_deeper():
#             print(value)
#
#         even_deeper()
#
#     print(value)
#     inner()
#     print(value)
#
#
# most_external()


#
# def most_external():
#     value = 5
#
#     def inner():
#         nonlocal value
#         value = 88
#         print(value)
#
#         def even_deeper():
#             print(value)
#
#         even_deeper()
#
#     print(value)
#     inner()
#     print(value)
#
#
# most_external()



# def most_external():
#     value = 5
#
#     def inner():
#         nonlocal value
#         value = 88
#         print(value)
#
#         def even_deeper():
#             value = 30
#             print(value)
#
#         even_deeper()
#
#     print(value)
#     inner()
#     print(value)
#
#
# most_external()


# def most_external():
#     value = 5
#
#     def inner():
#         nonlocal value
#         value = 88
#         print(value)
#
#         def even_deeper():
#             nonlocal value
#             value = 30
#             print(value)
#
#         even_deeper()
#
#     print(value)
#     inner()
#     print(value)
#
#
# most_external()


# def most_external():
#     value = 5
#
#     def inner():
#         value = 88
#         print(value)
#
#         def even_deeper():
#             nonlocal value
#             value = 30
#             print(value)
#
#         even_deeper()
#
#     print(value)
#     inner()
#     print(value)
#
#
# most_external()