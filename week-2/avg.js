function avg(data) {
    // 請用你的程式補完這個函式的區塊
    let salary = 0;
    let num = 0;
    data.employees.forEach(element => {
        if (element.manager == false) {
            salary += element.salary;
            num += 1;
        }
    });
    return salary / num;
}
avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": false
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": true
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": false
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": false
        }
    ]
}); // 呼叫 avg 函式

console.assert(avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": false
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": true
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": false
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": false
        }
    ]
}) === 40000, 'Wrong return.');