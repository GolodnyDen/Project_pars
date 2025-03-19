document.getElementById('search_button').addEventListener('click', function() {
    const jobTitle = document.getElementById('job_title').value.trim();
    const city = document.getElementById('city').value.trim();
    const company = document.getElementById('company').value.trim();

    if (!jobTitle || !city) {
        alert('Пожалуйста, заполните все обязательные поля.');
        return;
    }

    console.log('Отправляем запрос:', { jobTitle, city, company });

    fetch(`/search?job_title=${encodeURIComponent(jobTitle)}&city=${encodeURIComponent(city)}&company=${encodeURIComponent(company)}`)
        .then(response => {
            console.log('Получен ответ:', response);
            return response.json();
        })
        .then(data => {
            console.log('Данные:', data);
            const jobList = document.getElementById('job_list');
            jobList.innerHTML = '';
            if (data.jobs.length === 0) {
                jobList.innerHTML = '<p>Вакансии не найдены.</p>';
                return;
            }
            data.jobs.forEach(job => {
                const jobItem = document.createElement('div');
                jobItem.classList.add('job-item');
                jobItem.innerHTML = `
                    <h2>${job.title}</h2>
                    <p>Компания: ${job.company}</p>
                    <p>Зарплата: ${job.salary}</p>
                    <p>Опыт: ${job.experience}</p>
                    <p>Город: ${job.city}</p>
                `;
                jobList.appendChild(jobItem);
            });
        })
        .catch(error => {
            console.error('Ошибка при выполнении запроса:', error);
        });
});

