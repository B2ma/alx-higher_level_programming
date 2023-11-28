#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const todos = JSON.parse(body);

    // Filter completed tasks
    const completedTasks = todos.filter(task => task.completed);

    // Compute the number of completed tasks for each user
    const completedTasksByUser = completedTasks.reduce((result, task) => {
      if (result[task.userId]) {
        result[task.userId]++;
      } else {
        result[task.userId] = 1;
      }
      return result;
    }, {});

    // Print the result
    console.log(completedTasksByUser);
  }
});
