from pyquery import PyQuery

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
    assert 'Hi There' in q('#target').html(method='html')
    assert 'too-much-after' not in q('#target').html(method='html')
