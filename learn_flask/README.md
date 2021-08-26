### 关于响应
视图函数的返回值会自动转换为一个响应对象。如果返回值是一个字符串，那么会被 转换为一个包含作为响应体的字符串、一个 200 OK 出错代码 和一个 text/html 类型的响应对象。如果返回值是一个字典，那么会调用 jsonify() 来产生一个响应。以下是转换的规则：

1. 如果视图返回的是一个响应对象，那么就直接返回它。
2. 如果返回的是一个字符串，那么根据这个字符串和缺省参数生成一个用于返回的 响应对象。
3. 如果返回的是一个字典，那么调用 jsonify 创建一个响应对象。
4. 如果返回的是一个元组，那么元组中的条目可以提供额外的信息。元组中必须至少 包含一个条目，且条目应当由 (response, status) 、 (response, headers) 或者 (response, status, headers) 组成。 status 的值会重载状态代码， headers 是一个由额外头部值组成的列表 或字典。
5. 如果以上都不是，那么 Flask 会假定返回值是一个有效的 WSGI 应用并把它转换为 一个响应对象。

如果想要在视图内部掌控响应对象的结果，那么可以使用 make_response() 函数。

设想有如下视图:
```python
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

可以使用 make_response() 包裹返回表达式，获得响应对象，并对该对象 进行修改，然后再返回:

```python
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

### JSON 格式的 API
JSON 格式的响应是常见的，用 Flask 写这样的 API 是很容易上手的。如果从视图 返回一个 dict ，那么它会被转换为一个 JSON 响应。

```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

```
如果 dict 还不能满足需求，还需要创建其他类型的 JSON 格式响应，可以使用 jsonify() 函数。该函数会序列化任何支持的 JSON 数据类型。 也可以研究研究 Flask 社区扩展，以支持更复杂的应用。
```python
@app.route("/users")
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])
```

### 会话
```python
from flask import session

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```

