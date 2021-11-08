# Homework 7

In this assignment, we will get familiar with map reduce style algorithms.
You are welcome to setup Hadoop or use the MapReduce functionality in MongoDB,
or, you are welcome to use a simple MR library that I put together (see below).

## Dave's MR library MapperReducer

In the file `mapper_reducer.py` there is a simple tool for managing a MapReduce
"job".  While it doesn't scale (or even run anything in parallel), it does get
you to start thinking about the world as map and reduce tasks.  Feel free to
take a look under the hood, the code is not very complex.

To get you started, there are two main function in the `MapperReducer` class,
`map` and `reduce`. You will provide function to both for the MapperReducer to
run.  Let's see an example for word counting.  First we will discuss mapping
(extracted from `map_wc.py`.

    1: def map_it(emit, file_handle):
    2:     for line in file_handle:
    3:         for w0 in line.split():
    4:             w = re.sub('[^a-z]', '', w0.lower())
    5:             if w != '':
    6:                 emit(w, 1)

    7: mr = mapper_reducer.MapperReducer()
    8: mr.map(map_it, path)

Function `map_it` takes two arguments.  The first argument is a function
`emit`, which takes two parameters and emits the key and value pair, for example
see the line 6.  The second argument `file_handle` is a file handle,
which in python is iterable, for example see line 2.

Putting the pieces together, the code snippet takes a line of text, splits it on
white space. For each word, the snippet makes the word lower case and then
removes any non alpha-character.  Finally, if the word is not the empty string,
it emits the word and the count 1.  Similar to how we discussed in class

Putting the pieces together, in line 7, we instantiate a `MapperReducer` and run
`map` by providing the `map_it` function and the path to the files to process.

Next, let's discuss reducing (from `reduce_wc.py`).

    1: def reduce_it(emit, key, vals):
    2:     vals_as_ints = map(int, vals)
    3:     emit(key, sum(vals_as_ints))

    4: mr = mapper_reducer.MapperReducer()
    5: mr.reduce(reduce_it, sys.stdin)

Function `reduce_it` takes three arguments `emit`, which is the same as above,
`key`, which is the key to reduce for, and `values` an array of strings that are
all the values for the key.  Note that since the values are coming in as
strings, we will often have to change the type.  An example of how to do this as
a one liner is given in line 2.  As in class, we sum the values and emit the
result.

To run, just pipe the programs together:

     python map_wc.py | sort | python reduce_wc.py > results.txt

Note that since we are always emitting key value pairs, we can actually pipe
multiple steps. For example

     python map1.py | sort | python reduce1.py | sort | python reduce2.py


## Questions

Below are a few questions to get you some practice thinking about solving
problems with MapReduce style algorithms.

### Question 1

TF-IDF is a common method for assigning weights to words in Text mining
algorithms.  See [wikipedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) for a
more complete treatment.

In our first question, we will modify our word counting algorithm discussed in
class to compute TF-IDF for each word.

**What to submit** In a folder tfidf, all your code for computing TF-IDF via
MapReduce with a README.md explaining how to run.


### Question 2

Matrix-Vector product is a primitive operation used in many data mining
algorithms.

In this question, we will implement a MapReduce style algorithms for computing a
matrix vector product.  There is some sample data in the folder `data/mat-vec`
(and a python program that can help you generate more sample data.

**What to submit** In a folder `mat-vec`, all your code for computing matrix
vector products via MapReduce with a README.md explaining how to run.


### Question 3

Matrix Mult is another primitive operation used in many data mining algorithms.

In this question, we will implement a MapReduce style algorithms for computing a
matrix multiplication.  There is some sample data in the folder `data/mat-mat`
(and a python program that can help you generate more sample data.

**What to submit** In a folder `mat-mat`, all your code for computing matrix
vector products via MapReduce with a README.md explaining how to run.


### Question 4 (EC 3 points)

For extra credit implement matrix multiplication in SQL.  You can also implement
matrix multiplication in SQL.  Load two matrices into a relational database with
the schema

    Matrix
    - name string
    - row int
    - column int
    - value float

Write a SQL query that will multiply two matrices from the Matrix table.

**What to submit** In a folder mat-mat-sql, add file `query.sql` with the query
for matrix multiplication.

### What to submit

Put all your solutions in a folder `homework7`, tar and gzip it:

    tar cvzf homework7.tgz homework7

and upload to D2L. You have completed your last homework for the class.
Congrats!!!
