const Chat = require('./models/chat'); // Replace with your Mongoose model import

Chat.aggregate([
  {
    $unwind: "$messages" // Unwind the messages array to destructure it into separate documents
  },
  {
    $sort: { "messages.sentAt": -1 } // Sort messages within each chat by sentAt in descending order (latest message first)
  },
  {
    $group: {
      _id: "$_id", // Group by the chat's _id
      lastMessage: { $first: "$messages" }, // Select the first message (which is the latest due to previous sorting)
      otherFields: { $first: "$$ROOT" } // Preserve other fields of the chat document
    }
  },
  {
    $project: {
      _id: "$otherFields._id", // Rename _id field to match the chat document's _id
      otherFields: 1, // Include other fields of the chat document
      lastMessage: 1 // Include the latest message
    }
  },
  {
    $sort: { "lastMessage.sentAt": -1 } // Sort the chats by the sentAt of the last message in descending order
  }
], (err, sortedChats) => {
  if (err) {
    console.error(err);
    return;
  }

  // 'sortedChats' now contains the chat documents sorted by the date of the last sent message
  console.log(sortedChats);
});



const YourModel = require('./yourModel'); // Import your Mongoose model

YourModel.aggregate([
  // Unwind the array field to create a separate document for each element
  {
    $unwind: '$yourArrayField',
  },
  // Add your data to each element of the array
  {
    $set: {
      'yourArrayField.newField': 'yourDataToAdd', // Add your data here
    },
  },
  // Group the documents back into an array
  {
    $group: {
      _id: '$_id', // Group by the original document's _id
      yourArrayField: { $push: '$yourArrayField' },
      // You can include other fields from the original document here if needed
    },
  },
])
  .exec((err, result) => {
    if (err) {
      console.error(err);
      return;
    }
    // The modified array is in the 'result' variable
    console.log(result);
  });







const YourModel = require('./yourModel'); // Import your Mongoose model

YourModel.aggregate([
  // Unwind the array field to create a separate document for each element
  {
    $unwind: '$yourArrayField',
  },
  // Add your data to each element of the array
  {
    $set: {
      'yourArrayField.newField': 'yourDataToAdd', // Add your data here
    },
  },
  // Group the documents back into an array
  {
    $group: {
      _id: '$_id', // Group by the original document's _id
      yourArrayField: { $push: '$yourArrayField' },
      // You can include other fields from the original document here if needed
    },
  },
])
  .exec((err, result) => {
    if (err) {
      console.error(err);
      return;
    }
    // The modified array is in the 'result' variable
    console.log(result);
  });


