document.getElementById('check-member-submit').onclick = function() {
    let username = document.getElementById('check-member-username').value
    if (username === '') {
        return
    }
    fetch('http://127.0.0.1:3000/api/member?' + new URLSearchParams({ username }))
        .then(res => res.json())
        .then(result => {
            document.getElementById('check-member-username').value = '';
            if (result && !result.data) {
                document.getElementById('check-member-result').innerHTML = '';
                return;
            }
            let data = result.data;
            document.getElementById('check-member-result').innerHTML = `${data.name} (${data.username})`;
        })
        .catch(err => console.log(err));
};

document.getElementById('change-member-submit').onclick = function() {
    let name = document.getElementById('change-member-name').value
    if (name === '') {
        return
    }
    fetch('http://127.0.0.1:3000/api/member', {
        method: 'PATCH',
        body: JSON.stringify({ name }),
        headers: {
            'Content-type': 'application/json'
        }
    })
        .then(res => res.json())
        .then(result => {
            document.getElementById('change-member-name').value = '';
            if (result.hasOwnProperty('ok')) {
                document.getElementById('change-member-result').innerHTML = '更新成功';
                document.getElementById('welcome').innerHTML = `${name}，歡迎登入系統`;
            } else {
                document.getElementById('change-member-result').innerHTML = '更新失敗';
            }
        })
        .catch(err => console.log(err));
        
};