// Extracts comments that contains tasks assigned to the current user
function extractCommentsWithAssignedTasks() {
  // Gets the current document
  var doc = DocumentApp.getActiveDocument();
  var docId = doc.getId();
  var docUrl = doc.getUrl();

  // Gets current user's email
  var userEmail = Session.getActiveUser().getEmail();

  // Gets all comments within the current document
  var comments = Drive.Comments.list(docId, {
    'fields': 'comments(author(displayName),content,quotedFileContent,createdTime)'
  });
  
  var commentsWithAssignedTasks = [];

  var userTag = '@' + userEmail;

  if (comments.comments && comments.comments.length > 0) {
    comments.comments.forEach(function(comment) {
      if (comment.content && comment.content.indexOf(userTag) !== -1) { 
        commentsWithAssignedTasks.push({
          'assignee': userEmail,
          'assigner': comment.author.displayName,
          'content': comment.content,
          'quotedFileContent': comment.quotedFileContent.value,
          'createdTime': comment.createdTime,
          'sourceDocumentUrl': docUrl
        });
      }
    });
  }

  Logger.log(commentsWithAssignedTasks);
  storeAssignedTasks(commentsWithAssignedTasks);
}

// Store assigned tasks in a Google Sheet
function storeAssignedTasks(comments) {
  var sheet = SpreadsheetApp.create("Comments With Assigned Tasks").getActiveSheet();
  sheet.appendRow(['Assignee Email', 'Assigner', 'Task', 'Quoted File Content', 'Created Time', 'Source Document URL']);
  
  comments.forEach(function(comment) {
    sheet.appendRow([comment.assignee, comment.assigner, comment.content, comment.quotedFileContent, comment.createdTime, comment.sourceDocumentUrl]);
  });
}
  