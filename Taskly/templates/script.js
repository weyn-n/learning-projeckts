const input = document.getElementById("taskInput");
const button = document.getElementById("addButton");
const taskList = document.getElementById("taskList")

button.addEventListener("click",
    function () {

        const taskText = input.value;

        if (taskText === "") {
            return;
        }

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

        task.appendChild(checkbox);
        task.appendChild(text);
        task.appendChild(deleteButton);

        taskList.appendChild(task); // add on site

        input.value = "";
});
