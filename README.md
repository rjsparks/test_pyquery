# UPDATE
See https://github.com/gawel/pyquery/issues/230#issuecomment-1366704753. Using the method parameter with the html function avoids this issue.
----
# Exercising an issue with pyquery

This small repository shows an issue with pyquery's .html() methord on some platforms.

All tests pass on most environments, but on some, (Monterey m1 max, macports), errors like this appear:

```
(env) rjsparks@undex pyquery % tox -epy38
py38 installed: attrs==21.4.0,cssselect==1.1.0,distlib==0.3.4,filelock==3.5.1,iniconfig==1.1.1,lxml==4.7.1,packaging==21.3,platformdirs==2.5.0,pluggy==1.0.0,py==1.11.0,pyparsing==3.0.7,pyquery==1.4.3,pytest==7.0.1,six==1.16.0,toml==0.10.2,tomli==2.0.1,tox==3.24.5,virtualenv==20.13.1
py38 run-test-pre: PYTHONHASHSEED='801918821'
py38 run-test: commands[0] | pip install -r requirements.txt
Requirement already satisfied: pyquery in ./.tox/py38/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (1.4.3)
Requirement already satisfied: pytest in ./.tox/py38/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (7.0.1)
Requirement already satisfied: tox in ./.tox/py38/lib/python3.8/site-packages (from -r requirements.txt (line 3)) (3.24.5)
Requirement already satisfied: cssselect>0.7.9 in ./.tox/py38/lib/python3.8/site-packages (from pyquery->-r requirements.txt (line 1)) (1.1.0)
Requirement already satisfied: lxml>=2.1 in ./.tox/py38/lib/python3.8/site-packages (from pyquery->-r requirements.txt (line 1)) (4.7.1)
Requirement already satisfied: py>=1.8.2 in ./.tox/py38/lib/python3.8/site-packages (from pytest->-r requirements.txt (line 2)) (1.11.0)
Requirement already satisfied: packaging in ./.tox/py38/lib/python3.8/site-packages (from pytest->-r requirements.txt (line 2)) (21.3)
Requirement already satisfied: iniconfig in ./.tox/py38/lib/python3.8/site-packages (from pytest->-r requirements.txt (line 2)) (1.1.1)
Requirement already satisfied: pluggy<2.0,>=0.12 in ./.tox/py38/lib/python3.8/site-packages (from pytest->-r requirements.txt (line 2)) (1.0.0)
Requirement already satisfied: attrs>=19.2.0 in ./.tox/py38/lib/python3.8/site-packages (from pytest->-r requirements.txt (line 2)) (21.4.0)
Requirement already satisfied: tomli>=1.0.0 in ./.tox/py38/lib/python3.8/site-packages (from pytest->-r requirements.txt (line 2)) (2.0.1)
Requirement already satisfied: six>=1.14.0 in ./.tox/py38/lib/python3.8/site-packages (from tox->-r requirements.txt (line 3)) (1.16.0)
Requirement already satisfied: filelock>=3.0.0 in ./.tox/py38/lib/python3.8/site-packages (from tox->-r requirements.txt (line 3)) (3.5.1)
Requirement already satisfied: virtualenv!=20.0.0,!=20.0.1,!=20.0.2,!=20.0.3,!=20.0.4,!=20.0.5,!=20.0.6,!=20.0.7,>=16.0.0 in ./.tox/py38/lib/python3.8/site-packages (from tox->-r requirements.txt (line 3)) (20.13.1)
Requirement already satisfied: toml>=0.9.4 in ./.tox/py38/lib/python3.8/site-packages (from tox->-r requirements.txt (line 3)) (0.10.2)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in ./.tox/py38/lib/python3.8/site-packages (from packaging->pytest->-r requirements.txt (line 2)) (3.0.7)
Requirement already satisfied: platformdirs<3,>=2 in ./.tox/py38/lib/python3.8/site-packages (from virtualenv!=20.0.0,!=20.0.1,!=20.0.2,!=20.0.3,!=20.0.4,!=20.0.5,!=20.0.6,!=20.0.7,>=16.0.0->tox->-r requirements.txt (line 3)) (2.5.0)
Requirement already satisfied: distlib<1,>=0.3.1 in ./.tox/py38/lib/python3.8/site-packages (from virtualenv!=20.0.0,!=20.0.1,!=20.0.2,!=20.0.3,!=20.0.4,!=20.0.5,!=20.0.6,!=20.0.7,>=16.0.0->tox->-r requirements.txt (line 3)) (0.3.4)
py38 run-test: commands[1] | pip list
Package      Version
------------ -------
attrs        21.4.0
cssselect    1.1.0
distlib      0.3.4
filelock     3.5.1
iniconfig    1.1.1
lxml         4.7.1
packaging    21.3
pip          22.0.3
platformdirs 2.5.0
pluggy       1.0.0
py           1.11.0
pyparsing    3.0.7
pyquery      1.4.3
pytest       7.0.1
setuptools   60.6.0
six          1.16.0
toml         0.10.2
tomli        2.0.1
tox          3.24.5
virtualenv   20.13.1
wheel        0.37.1
py38 run-test: commands[2] | pytest
============================= test session starts ==============================
platform darwin -- Python 3.8.12, pytest-7.0.1, pluggy-1.0.0
cachedir: .tox/py38/.pytest_cache
rootdir: /Users/rjsparks/tmp/pyquery
collected 1 item

test_pyquery.py F                                                        [100%]

=================================== FAILURES ===================================
_________________________________ test_pyquery _________________________________

    def test_pyquery():
        doc = \
    """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>title</title>
      </head>
      <body>
       <table>
         <tbody>
          <tr id="too-much-before">
            <th></th>
            <td></td>
          </tr>
          <tr id="target">
            <th>Hi There</th>
            <td></td>
          </tr>
          <tr id="too-much-after">
            <th></th>
            <td></td>
        </tbody>
      </table>
      </body>
    </html>
    """
        q = PyQuery(doc)
        assert 'Hi There' in q('#target').html()
>       assert 'too-much-after' not in q('#target').html()
E       assert 'too-much-after' not in '\n        <...td/>\n      '
E         'too-much-after' is contained here:
E             <tr id="too-much-after">
E                   <th/>
E                   <td/>
E               </tr></tbody>
E             </table>
E             </body>...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

test_pyquery.py:32: AssertionError
=========================== short test summary info ============================
FAILED test_pyquery.py::test_pyquery - assert 'too-much-after' not in '\n    ...
============================== 1 failed in 0.04s ===============================
ERROR: InvocationError for command /Users/rjsparks/tmp/pyquery/.tox/py38/bin/pytest (exited with code 1)
___________________________________ summary ____________________________________
ERROR:   py38: commands failed
```

