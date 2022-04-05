from tracer import tracefunc


@tracefunc
def show_args_and_kwargs(*args, **kwargs):
    return


if __name__ == "__main__":

    show_args_and_kwargs(10)
    show_args_and_kwargs(color="Red")
    show_args_and_kwargs(10, 200, color="Blue", type="Dog")