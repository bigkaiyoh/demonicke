import streamlit as st
import time

#Page Configuration
st.set_page_config(
    page_title = "Demonicke",
    page_icon = "🧠",
    layout = "wide"
)

# Sample Questions
IELTS_SAMPLE_QUESTION = "Write about the following topic.Some people think living in big cities is bad for people’s health.To what extent do you agree or disagree?Give reasons for your answer and include any relevant examples from your own knowledge or experience."
TOEFL_SAMPLE_QUESTION = "How do we overcome stereotypes?"
GENERAL_SAMPLE_QUESTION = "Today, some companies have online interviews for people who apply for jobs. Do you think this is a good idea?"

# Sample Inputs
IELTS_SAMPLE_INPUT = """
To what extent can living in a large city be unhealthy?
 Living in a large metropolitan can bring many challenges to one's health. When you live and work in a never-ending rat race there can be consequences to your health becasue of the continuous stress brought on by increased workload, longer working hours and very little time to rest.
 There is also an increase in pollution due to the high density of people, cars and other carbon immisions.
 I agree to an extent that living in a big city can bring about its challenges to your health, however, there are many more advantages to living in a major city when ones health takes a dip rather than being ill in a rural or outlying area. Getting sick and having health issues is not bound by an area you live in. These things happen to us no matter where we live. Living stress free in a rural area does not take away the fact that I may carry a cancer gene.
 In my experience living in both an outlaying area and a city, when I needed to see a specialist for a health condition, I had to travel many hours to a doctor in the metropolitain area. These types of highly qualified doctors do not practise in rural areas or areas that are outside of a bit city. Generally speaking a specialist will be in a metro area where there is access to state of the art hospitals.
 Do I believe that living in a city can bring on certain illnesses? Yes, defrinatly.
 I would much rather live in a big city where all my health needs can be easily accessed rather than in an area out of the city where I may not get the medical attention I need.
"""

TOEFL_SAMPLE_INPUT = """
Overcoming stereotypes 
“I bet people are drinking tea ALL the time” “They all sound so posh, don’t they?” This is what my Japanese friends around me say about England. Their impressions of the British seem to be based on generalized symbols such as the Royal Family and afternoon tea, and although they are a huge part of its culture, they do not fully epitomize its people. This is a story about how four years of living in Britain made me realize the imbecility of judging people and generalizing them with stereotypes based on their ethnicity. 
Looking back, my time as a student at an all-girls British private school remains one of the most enchanting and enriching memories of my life. Everything differed immensely from the school I attended in Japan, but what struck me most was that each grade consisted of around ten girls. It really fostered an intense sense of unity and connection throughout the school. I got to know each of them well and they made up a huge part of my childhood. 
However, on my first day of school, I did have a fear of getting picked on by being the ‘odd’ one out. The eight-year-old me was expecting a British school to be full of children who had oceandeep blue eyes and shimmering blonde hair - or at least, that was how London was depicted in a book I read when I was a toddler. I assumed that I would be the only one who wasn’t fluent in English, with pitch-black eyes and brownish hair. But actually, things were very different. 12 girls from various countries such as England, India, China, Africa, Japan, and South Korea, were all gathered inside a classroom, and I was astounded by the amount of diversity which I had never encountered in Japan. Nobody treated me differently because I was ‘Japanese,’ they just talked to me because I was new, and even offered to help me with my awkward English. 
Spending time with these 12 girls at school fluctuated all the stereotypes that I had inside me over time. For example, the only interaction I had with Chinese people was hearing them jabber on about something on the street, so I thought they were aggressive and loud, also being math wizards like my dad had told me. But Hei-Lam, who was a Chinese girl in my class was the quietest and was so sophisticated (yes, a math wizard) that she skipped grades. But her sister, Hei-Tou, was so cheeky and bubbly that she often got scolded by the teacher. It really wasn’t about their race. Moreover, there were two Indian girls named Prisha and Preet, who both believed in Hinduism. Because I had thought Indians were not allowed to eat meat based on their religion, I gaped when Preet only put potatoes and vegetables on the plate but Prisha gobbled down a slice of roast beef. Seeing my worried face, she chuckled and kindly told me, “Not all Hindus are vegetarians Miyu, some eat dairy but not meat, and some reject both. I’m a Hindu but I still eat meat.” All these experiences gradually instilled the importance of dispelling stereotypes as they often did not reflect reality. These experiences gradually impressed upon me the importance of dispelling stereotypes as they often do not align with reality. Each of these girls was different, unique, and beautiful in her own way. Their personalities might be influenced by their upbringing, but never solely by the color of their skin or the type of passport they hold.
 To address the questions posed at the beginning, not all British people are tea enthusiasts, nor do they all talk like the Royal Family. My journey through the halls of a British school shattered these preconceived notions and replaced them with the vivid reality that individuals are defined by their unique stories, aspirations, and personalities. By embracing curiosity and open-mindedness, I believe we can embark upon a world where people are valued for their unique identities, rather than harmful generalizations. Our shared experiences, shared stories, and shared humanity, can be the keys to unlocking a world free from the shackles of stereotypes. 
"""
GENERAL_SAMPLE_INPUT = """"
I think doing job interviews on internet is a good idea. There are some reasons. First, people who is looking for jobs are usually very busy. So if they don't have to go to actual places to take interviews, it will save their time a lot. Second, Many people who is finding jobs are usually want to save money. If they can take online interviews, they can spare their money. From these reasons, I think online interviews are good.
"""

# Sample Evaluations
IELTS_SAMPLE_EVALUATION = """
**Overall Band Score:** 6.0

**Task Achievement/Response:** 6
- Justification: The essay addresses the topic, presenting agreement that living in a big city can be unhealthy but also recognizing advantages regarding healthcare accessibility in cities. Yet, the response could be developed further by presenting specific examples and a broader range of reasons supporting the argument for a more comprehensive discussion related to health issues in big cities versus rural areas.

**Coherence and Cohesion:** 6
- Justification: The essay displays an overall logical structure with clear paragraphs, each focusing on different aspects of health challenges and benefits in big city living. However, the transitions between ideas could be smoother, and the argument would benefit from more explicit connections between points to enhance coherence.

**Lexical Resource:** 6
- Justification: The response uses a variety of vocabulary appropriately and with flexibility in some places (""rat race,"" ""carbon emissions,"" ""state of the art hospitals""). However, there are spelling errors (""defrinatly"" should be ""definitely,"" ""immisions"" should be ""emissions"") and some word choice issues that affect clarity (""outlaying"" should be ""outlying"", ""bit city"" possibly meant ""big city""). To achieve a higher score, more sophisticated vocabulary and accurate spelling are needed.

**Grammatical Range and Accuracy:** 6
- Justification: The essay demonstrates a mix of simple and complex sentence structures. Nevertheless, grammatical mistakes (""becasue"" instead of ""because"", ""an increase in pollution due to the high density of people, cars and other carbon immisions"" could be smoother) and punctuation errors hinder the overall accuracy. The writer should focus on enhancing grammatical accuracy through more careful proofreading and practice with complex sentences.

---

**Recognize Strengths:**
- You've successfully presented a nuanced view, acknowledging both the health challenges and healthcare benefits associated with living in a big city. Your personal example of needing to travel for specialist care effectively supports your argument.

**Identify and Explain Errors:**
- Spelling errors such as ""defrinatly"" for ""definitely"" and ""becasue"" for ""because"" detract from the essay's quality. Correcting these would enhance readability.
- ""an increase in pollution due to the high density of people, cars and other carbon immisions"" can be refined to ""an increase in pollution due to the high density of people, vehicles, and carbon emissions"" for clarity and accuracy.

**Advanced Language Suggestions:**
- Consider using more nuanced expressions, for example: ""Indeed, city living does pose certain health risks, notably due to pervasive stress factors and exacerbated pollution levels.""
- To improve lexical resource score, incorporate less common idioms or phrases: ""While the urban milieu is a double-edged sword for health, the availability of advanced medical facilities somewhat mitigates these drawbacks.""

**Continuous Improvement Plan:**
- To enhance your grammatical range and accuracy, dedicate practice time to complex sentence constructions. Work on exercises that focus on compound and complex sentences, as well as punctuation.
- Regular reading of high-quality articles or books on urban living can provide insights into sophisticated vocabulary and structures that can be emulated in your writing.
"""
TOEFL_SAMPLE_EVALUATION = """"
**Overall Score:** 4

**Development:** 4
- Justification: The essay has a clear main idea that stereotypes are harmful and it articulates several instances from the writer's experience to support this. The experiences with classmates from diverse backgrounds serve as specific details enhancing the development of this key argument. However, more connection between these instances and a broader analysis of overcoming stereotypes beyond personal anecdotes could further strengthen the piece.

**Organization:** 4
- Justification: The organization of the essay is logical, moving from an anecdotal introduction to more detailed personal stories, and closing with a broader reflection on the lessons learned. Paragraphs are structured around distinct ideas, making it easy for the reader to follow. The transition between paragraphs could be smoother with more explicit linking phrases to enhance coherence.

**Language Use:** 4
- Justification: The language use is mostly effective with a combination of simple and complex sentence structures. Vocabulary is varied and generally precise, contributing to the clarity of the essay. There are minor errors and areas where more sophisticated language could be used, such as varying verb structures and integrating more advanced vocabulary relating to the topic of stereotypes and cultural understanding.

---

**Recognize Strengths:** The essay does an excellent job of integrating personal anecdotes to challenge stereotypes, which makes the argument compelling and relatable. The reflection on personal growth and change in perspective is a strong narrative element that enriches the essay.

**Identify and Explain Errors:** The essay occasionally resorts to general statements without providing a direct analysis or conclusion on overcoming stereotypes on a broader scale. For instance, discussing strategies for overcoming stereotypes outside of personal growth could offer a more comprehensive view.

**Advanced Language Suggestions:** To elevate the writing sophistication, consider using more nuanced language to describe personal transformations and cultural insights. For example, instead of saying ""dispelling stereotypes,"" you might say ""dismantling preconceived notions."" Complex sentence structures, such as conditional sentences, could also add depth, e.g., ""Had I not been exposed to such diversity, I might have continued to harbor unfounded stereotypes.""

**Feedback on Structure and Organization:** The essay's structure is sound, but integrating a clear thesis statement at the beginning and a concluding statement that ties all personal anecdotes back to the overarching theme of overcoming stereotypes could improve it. Moreover, explicitly introducing each anecdote with a sentence that sets the context for how it challenges a specific stereotype would help in organizing paragraphs more effectively.

**Encourage Self-Reflection:** Reflect on how the personal experiences shared in the essay can translate into broader strategies for addressing and overcoming stereotypes in different contexts. Consider writing about how these insights might apply in professional, educational, and social settings.

**Continuous Improvement Plan:** Continue to read widely on topics related to cultural understanding and the psychology of stereotypes. Writing practice that focuses on discussing solutions to cultural misunderstandings or proposing methods for encouraging diversity and inclusion could be beneficial. Participating in forums or discussions on these topics can also offer new perspectives and vocabulary to incorporate into your writing.
"""
GENERAL_SAMPLE_EVALUATION = """
**CEFR Level:** A2
**Score:** 70

**Balanced Feedback:**  
Your writing does a great job of conveying your opinion on online interviews straightforwardly, with a clear structure leading your arguments. You've effectively used examples to support your viewpoints, which strengthens your argument. However, there are areas for improvement in grammar and coherence to elevate your writing further.

**Strengths:**  
- **Clarity of Opinion:** You've made your stance on online interviews clear, which is excellent for persuasive writing.  
- **Organization:** You structured your argument in a logical manner, introducing your thesis and then supporting it with examples.  

**Areas to Grow:**
- **Grammar and Usage:** Be mindful of verb agreement (e.g., ""people who is"" should be ""people who are"") and word choice (""on internet"" should be ""on the internet"").
- **Vocabulary Enhancement:** Expanding your vocabulary and using varied sentence structures could make your writing more engaging.
  
**Enhanced Vocabulary Table:**
| Current Expression | Suggested Advanced Phrase | Example Usage |
|-------------------|---------------------------|---------------|
| good idea         | beneficial                | I think doing job interviews on the internet is beneficial. |
| looking for jobs  | job searching             | People job searching are often very busy. |
| want to save money| seek to economize         | Many people looking for jobs seek to economize. |

**Sample Improvement:**  
I believe conducting job interviews over the internet is beneficial for several reasons. Firstly, individuals who are actively job searching are typically very busy. Therefore, if they can participate in interviews online and eliminate the need to travel physically, it will significantly save their time. Furthermore, many job seekers are also looking to economize. Online interviews allow them to save money, which might be spent on commuting or other expenses related to in-person interviews. Considering these points, online interviews offer a pragmatic solution for both employers and applicants.

**Engagement and Motivation:**  
Why not explore more about the impact of technology on various industries? You could write a short essay or paragraph about another technological innovation that has changed the way we work or live. This could help you practice your argumentative writing skills and explore new vocabulary.
"""

SAMPLE_QUESTIONS = {
    "IELTS": IELTS_SAMPLE_QUESTION,
    "TOEFL": TOEFL_SAMPLE_QUESTION,
    "General": GENERAL_SAMPLE_QUESTION
}

SAMPLE_INPUTS = {
    "IELTS": IELTS_SAMPLE_INPUT,
    "TOEFL": TOEFL_SAMPLE_INPUT,
    "General": GENERAL_SAMPLE_INPUT
}

SAMPLE_EVALUATIONS = {
    "IELTS": IELTS_SAMPLE_EVALUATION,
    "TOEFL": TOEFL_SAMPLE_EVALUATION,
    "General": GENERAL_SAMPLE_EVALUATION
}



def set_test_configuration():
    option = st.selectbox(
        "Choose Test Framework",
        ("IELTS", "TOEFL", "General"),
        index=0,
        placeholder="Select the test"
    )
    return option

def get_question_input(option):
    question = st.text_input("Question (optional)", value=SAMPLE_QUESTIONS[option])
    return question

def get_user_input(option):
    answer = st.text_area("Your Answer for Evaluation", value=SAMPLE_INPUTS[option], height=200)
    return answer

def display_sample_evaluation(option, question, user_input, container):
    container.empty()  # Clear the initial message
    with st.container(height=800, border=False):
        if question:  # Concatenate question and answer if question is provided
            user_input = f"Question: {question}\n\nAnswer: {user_input}"
        
        with st.spinner('Neurons weaving through the layers...'):
            time.sleep(2)  # Simulate processing delay

        st.chat_message("user").write(user_input)  # Display user input
        st.chat_message("assistant").write(SAMPLE_EVALUATIONS[option])  # Display evaluation

def main():
    st.title("Demo with Samples")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://nuginy.com/wp-content/uploads/2024/01/23f602002a0787321609a4bf3b8ef051.png", use_column_width="auto")
        option = set_test_configuration()
        question = get_question_input(option)
        user_input = get_user_input(option)
        submit_button = st.button("Grade it!", key="grade_it")

    with col2:
        st.header("Feedback")
        temporary = st.empty()
        with temporary.container():
            st.chat_message("assistant").write("Today is a blank canvas waiting for your linguistic masterpiece.")
        
        if submit_button:
            display_sample_evaluation(option, question, user_input, temporary)

if __name__ == "__main__":
    main()
