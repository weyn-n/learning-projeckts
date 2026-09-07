const checkboxes = document.querySelectorAll(".task input[type='checkbox']");

checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener("change", function() {
        const task = checkbox.parentElement;

        task.classList.toggle("completed");
    });
});