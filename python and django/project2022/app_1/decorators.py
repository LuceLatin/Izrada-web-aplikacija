from django.shortcuts import redirect


def admin_required(function):
    def wrap(*args, **kwargs):
        #print(args[0].user)
        #print(args[0].user.role.role)
        if args[0].user.role.role == Role.ADMIN:
            return function(*args, **kwargs)
        else:
            return redirect('register')
    return wrap


""" def student_required(function):
    def wrap(*args, **kwargs):
        print(args[0].user)
        print(args[0].user.role.role)
         if args[0].user.role.role == Role.STUDENT:
            return function(*args, **kwargs)
        else:
            return redirect('register')
    return wrap


def profesor_required(function):
    def wrap(*args, **kwargs):
        #print(args[0].user)
        #print(args[0].user.role.role)
        if args[0].user.role.role == Role.PROFESOR:
            return function(*args, **kwargs)
        else:
            return redirect('register')
    return wrap  """