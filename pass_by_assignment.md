### Technically, Python uses “pass by assignment.” This is like call-by-value, in that you can do this

```>def plus_1(x) :
>  x=x+1
>
>x=5
>plus_1(x)
>print x
5
```
Here, x was passed by value - local changes within the function didn’t echo back to the calling scope.

However, if we use a list, elements are passed by reference. So that here,

```>def plus_1(x) :
>  x[0]=x[0]+1
>
>x=[5]
>plus_1(x)
>print x[0]
6
```
So we can think of it as a “shallow copy”. A change to any list element will be reflected back, but if we change the “top level” - blast away the list itself, that change won’t be seen outside the function. So while x[0]=99 gets passed back, x = [55,66] won’t.

This works for any mutable data type like a dictionary or an object you defined in a class.