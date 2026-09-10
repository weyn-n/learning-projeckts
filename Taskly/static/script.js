const input = document.getElementById("taskInput");
const button = document.getElementById("addButton");
const taskList = document.getElementById("taskList")

if (input && button && taskList) {

    button.addEventListener("click",
        function () {

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
                console.log(data);    
            });

            // create card
            const task = document.createElement("div");
            task.classList.add("task");

            // create checkbox
            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";

            // create text
            const text = document.createElement("span");
            text.textContent = input.value;

            // create delete button
            const deleteButton = document.createElement("button");
            deleteButton.textContent = "🗑";

            // checkbox
            checkbox.addEventListener("change", function () {

                if (checkbox.checked) {
                    text.style.textDecoration = "line-through";
                } else {
                    text.style.textDecoration = "none";
                }

            });

            deleteButton.addEventListener("click", function () {
                task.remove();
            });

            task.appendChild(checkbox);
            task.appendChild(text);
            task.appendChild(deleteButton);

            taskList.appendChild(task); // add on site

            input.value = "";
    });

}