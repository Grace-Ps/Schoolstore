// script.js
document.addEventListener("DOMContentLoaded", function () {
    const departmentSelect = document.getElementById("department");
    const courseSelect = document.getElementById("courses");

    departmentSelect.addEventListener("change", function () {
        const selecteddepartmentId = departmentSelect.value;
        fetch(`/get_Courses/${selecteddepartmentId}/`)
            .then((response) => response.json())
            .then((data) => {
                courseSelect.innerHTML = '<option value="">Select a course</option>';
                data.forEach((course) => {
                    const option = document.createElement("option");
                    option.value = course.id;
                    option.textContent = course.name;
                    courseSelect.appendChild(option);
                });
            });
    });
});
