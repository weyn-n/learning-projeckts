const input = document.getElementById("taskInput");
const button = document.getElementById("addButton");
const taskList = document.getElementById("taskList");

if (input && button && taskList) {

    // create Task
    function createTask(id, title) {

        const task = document.createElement("div");
        task.classList.add("task");

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";

        const text = document.createElement("span");
        text.textContent = title;

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "🗑";

        checkbox.addEventListener("change", function () {
            if (checkbox.checked) { 
                
                text.style.textDecoration = "line-through";
            
                fetch(`/api/tasks/${id}`, {
                    method: "PUT"
                });   
            }  
        });

        deleteButton.addEventListener("click", function () {
            fetch(`/api/tasks/${id}`, {
                method: "DELETE"
            })
            .then(response => response.json())
            .then(data => {
                task.remove();
            });
        });

        task.appendChild(checkbox);
        task.appendChild(text);
        task.appendChild(deleteButton);

        taskList.appendChild(task);
    }


    // GET
    fetch("/api/tasks")
        .then(response => response.json())
        .then(data => {
            data.forEach(task => {
                createTask(task[0], task[1]);
            });
        });


    // POST
    button.addEventListener("click", function () {

        const taskText = input.value;

        if (taskText === "") {
            return;
        }

        fetch("/api/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                title: taskText
            })
        })
        .then(response => response.json())
        .then(data => {
            createTask(data.id, data.title);
        });

        input.value = "";
    });

}