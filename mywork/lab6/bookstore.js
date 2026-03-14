// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  name: "Jane Austen",
  nationality: "British",
  bio: {
    short: "English novelist known for novels about the British landed gentry.",
    long: "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
  { name: "Jane Austen" },
  { $set: { birthday: "1775-12-16" } }
)

// Task 5: insert four more authors
db.authors.insertMany([
{
  name: "George Orwell",
  nationality: "British",
  bio: {
    short: "English novelist and essayist known for political fiction.",
    long: "George Orwell wrote Animal Farm and 1984."
  },
  birthday: "1903-06-25"
},
{
  name: "Mark Twain",
  nationality: "American",
  bio: {
    short: "American writer known for humor and satire.",
    long: "Mark Twain wrote Tom Sawyer and Huckleberry Finn."
  },
  birthday: "1835-11-30"
},
{
  name: "Chinua Achebe",
  nationality: "Nigerian",
  bio: {
    short: "Nigerian novelist famous for Things Fall Apart.",
    long: "Achebe helped shape modern African literature."
  },
  birthday: "1930-11-16"
},
{
  name: "Haruki Murakami",
  nationality: "Japanese",
  bio: {
    short: "Japanese novelist known for surreal fiction.",
    long: "Murakami wrote Norwegian Wood and Kafka on the Shore."
  },
  birthday: "1949-01-12"
}
])

// Task 6: total count
db.authors.countDocuments({})

// Task 7: British authors sorted by name
db.authors.find({ nationality: "British" }).sort({ name: 1 })
