# Купи слона

agree = ["хорошо", "давай", "да", "окей", "ок", "куплю", "уговорил"]
pros = ["Слоник такой замечательный.", "Он детей на себе катает.",
        "Он на задние ноги встаёт по команде.", "Он утром нежно хобот на грудь кладёт.",
        "Чудо, а не слон."]


def elephant():
    """
    Агитирует купить слона до тех пор пока не получиит положительного ответа в инпуте.
    """
    i = 0
    while i < 5:
        print('Купи слона. ' + pros[i])
        i += 1
        if input().lower() in agree:
            break

# Fibonacci


def fibonacci_iter(n):
    """
    Возвращаает элементы последовательности Фибоначчи для заданной длины.
    >>> fibonacci_iter(7)
    0 1 1 2 3 5 8
    """
    first = 0
    second = 1
    print(first, end=' ')
    print(second, end=' ')
    for i in range(2, n):
        first, second = second, first + second
        print(second, end=' ')


def fibonacci(n: int):
    """
    Возвращает число по индексу из последовательности Фибоначчи.
    >>> fibonacci(6)
    5
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(elephant())
    print(fibonacci_iter(7))
    print(fibonacci(6))
