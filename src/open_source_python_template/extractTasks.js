function extractCommentsWithAssignedTasks() {
    var doc = DocumentApp.getActiveDocument();
    var docId = doc.getId();
    var userEmail = Session.getActiveUser().getEmail();
    var comments = Drive.Comments.list(docId, {
      'fields': 'comments(author(displayName),content,createdTime)'
    });
    
    var commentsWithAssignedTasks = [];
    
    if (comments.comments && comments.comments.length > 0) {
      comments.comments.forEach(function(comment) {
        if (comment.content && comment.content.indexOf(userEmail) !== -1) { 
          commentsWithAssignedTasks.push({
            'assigner': comment.author.displayName,
            'content': comment.content,
            'time': comment.createdTime
          });
        }
      });
    }
  
    Logger.log(commentsWithAssignedTasks);
    storeAssignedTasks(commentsWithAssignedTasks);
}
  
function storeAssignedTasks(comments) {
    var sheet = SpreadsheetApp.create("Comments With Assigned Tasks").getActiveSheet();
    sheet.appendRow(['Assigner', 'Comment', 'Time']);

    comments.forEach(function(comment) {
        sheet.appendRow([comment.assigner, comment.content, comment.time]);
    });
}
  