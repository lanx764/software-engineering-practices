1. def d is a long function and it is dangerous because when it breaks you will have no idea which of its responsibilities that caused the failure
2. 
    if len(bad) > 0:
        print("alert") have magic number and magic strings becuase when one come backs to the code later no one will have the idea of where alert,0 and 500 came from and "%Y-%m-%d" is also a magic string.
3. There also dead codes which the functions takes as parameter r,l and c and it is dangerous because It makes a reader wonder whether that block was intentional, whether it is safe to delete, whether it represents an old approach that was abandoned or a future feature that was never finished.
 for index, row in df.iterrows():
     if row["v"] < 0:
         bad.append(row) is a dead code also because it is a commented out logic that was never used 
4. there is also a duplicate code issue here becuase when you duplicate duplicate a code and the logic changes you dont have to miss anything from the previous function or else you have introduced a silent bug and if you look at both functions here the second function is missing some responsibilities
5. the first function is a God object it know too much/does too much and it is untestable and unextendable and when it breaks the entire sysytem breaks with it
6. and the functions also have long parameter list it is also a signal that the function is doing too much 
7. it has a speculative generality issue also because there are some parameter in the functions that they were never called
8.  for index, row in df.iterrows():
         if row["v"] < 0:
             bad.append(row) this comment only shows what and not why