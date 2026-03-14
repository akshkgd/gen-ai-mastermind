import OpenAI from "openai";
import 'dotenv/config';
const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-4.1-mini",
  input: [
    {
        role: "system",
        content: `you are an Teaching assistant of codekaro with the goal to help students ask thier javascript questions or any question from given FAQ. if the user asks anything apart from javascript do not answer and mention u can only help with js doubts. 
        FAQs:
        question: what courses u have? answer: we have fullstack and genAi courses.
        question: can a freher enroll in it? answer: yes we will cover everthing from scratch`
    },
    {
        role: "user",
        content: "what course can i enroll??"
    }

  ]
});

console.log(response.output_text);
