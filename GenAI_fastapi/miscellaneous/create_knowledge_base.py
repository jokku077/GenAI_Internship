import pymongo
from datetime import datetime

def create_chatbot_knowledge_base():
    client = pymongo.MongoClient(
        "mongodb+srv://jokku7110:jokkumongoatlas@cluster0.7s1xk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        tls=True,
        tlsAllowInvalidCertificates=True)  # Use `tls` instead of `ssl` # Update with your DB URI #mongodb://localhost:27017/

    db = client["Genai_fastapi"]

    # # Drop existing collection if it exists (for clean setup)
    # if "chatbotdb" in db.list_collection_names():
    #     db["knowledge_base"].drop()

    # Create knowledge_base collection
    knowledge_base = db["chatbotdb"]

    # Create a text index on the question field for better searching
    knowledge_base.create_index([("question", pymongo.TEXT)])

    # Populate with sample Q&A pairs
    sample_data = [
        # Product Information
        {
            "question": "What products do you offer?",
            "answer": "We offer a range of products including smartphones, laptops, tablets, and accessories. Our most popular lines are the Galaxy series smartphones, the UltraBook laptops, and the TabPro tablets."
        },
        {
            "question": "How much does the UltraBook Pro cost?",
            "answer": "The UltraBook Pro starts at $1,299 for the base model with 16GB RAM and 512GB SSD. The premium model with 32GB RAM and 1TB SSD is priced at $1,799."
        },
        {
            "question": "What are the specifications of the Galaxy S23?",
            "answer": "The Galaxy S23 features a 6.1-inch Dynamic AMOLED display, Snapdragon 8 Gen 2 processor, 8GB RAM, options for 128GB or 256GB storage, a triple camera system (50MP main, 12MP ultrawide, 10MP telephoto), and a 3,900mAh battery with fast charging support."
        },

        # Customer Support
        {
            "question": "How do I return a product?",
            "answer": "To return a product, please visit our Returns Center at example.com/returns within 30 days of receiving your order. You'll need your order number and the email address used for the purchase. We offer free return shipping for defective items, and a prepaid return label for a $5 fee for other returns."
        },
        {
            "question": "How long is the warranty period?",
            "answer": "Our standard warranty is 1 year from the date of purchase for manufacturing defects. Premium products like the UltraBook Pro and Galaxy S23 come with an extended 2-year warranty. You can also purchase additional warranty coverage for up to 3 more years through our Protection Plan."
        },
        {
            "question": "How can I track my order?",
            "answer": "You can track your order by visiting our Order Tracking page at example.com/track and entering your order number and email address. You should have received an order confirmation email with your order number. Alternatively, if you have an account, you can check the status in your account dashboard."
        },

        # Account & Billing
        {
            "question": "How do I reset my password?",
            "answer": "To reset your password, visit example.com/account/password-reset and enter the email address associated with your account. We'll send you a password reset link that will be valid for 24 hours. Click the link and follow the instructions to create a new password."
        },
        {
            "question": "What payment methods do you accept?",
            "answer": "We accept Visa, Mastercard, American Express, Discover, PayPal, and Apple Pay. For orders over $500, we also offer financing options through Affirm with 0% interest for qualified customers. All payments are processed securely through our encrypted payment system."
        },
        {
            "question": "Do you offer discounts for students?",
            "answer": "Yes, we offer a 15% discount for verified students. To receive your student discount, please register with your school email address at example.com/student-discount and verify your status through our education verification partner. The discount will be applied automatically to your account for one year."
        },

        # Technical Support
        {
            "question": "How do I connect my Galaxy S23 to Wi-Fi?",
            "answer": "To connect your Galaxy S23 to Wi-Fi: 1) Open Settings, 2) Tap on 'Connections', 3) Tap on 'Wi-Fi' and toggle it on, 4) Select your Wi-Fi network from the list, 5) Enter the password if prompted, and tap 'Connect'. Your phone will remember this network for future automatic connections."
        },
        {
            "question": "My UltraBook won't turn on, what should I do?",
            "answer": "If your UltraBook won't turn on, try these steps: 1) Make sure it's charged by connecting the power adapter and check if the charging light is on, 2) Press and hold the power button for 10 seconds, release, then press once to turn on, 3) If it still doesn't respond, try disconnecting the battery (if possible) for 30 seconds, then reconnect and try again, 4) If these steps don't work, please contact our technical support at support@example.com."
        },
        {
            "question": "How do I update the software on my device?",
            "answer": "To update your device software: For smartphones and tablets, go to Settings > Software Update > Download and Install. For UltraBook laptops, open the Update Assistant app from the Start menu and click 'Check for Updates'. We recommend keeping your devices updated for the latest features and security improvements."
        },

        # Store Information
        {
            "question": "What are your store hours?",
            "answer": "Our physical stores are open Monday through Saturday from 10 AM to 9 PM, and Sunday from 11 AM to 6 PM. Hours may vary during holidays, so please check our store locator at example.com/stores for specific location details. Our online store is available 24/7."
        },
        {
            "question": "Do you have stores in Canada?",
            "answer": "Yes, we currently have 15 store locations across Canada, with presence in Toronto, Vancouver, Montreal, Calgary, Edmonton, and Ottawa. You can find the nearest store using our store locator at example.com/stores/canada. All Canadian stores offer the same services and warranty support as our US locations."
        },
        {
            "question": "Do you offer in-store repairs?",
            "answer": "Yes, all of our retail locations offer in-store technical services and repairs. Most minor repairs can be done same-day if parts are in stock. For more complex repairs, devices typically need to be sent to our repair center with a 3-5 business day turnaround. We recommend making an appointment online at example.com/support/repair before bringing your device in."
        },

        # Policies
        {
            "question": "What is your privacy policy?",
            "answer": "Our privacy policy details how we collect, use, and protect your personal information. In summary, we collect basic account info, purchase history, and device usage data to improve our services. We never sell your personal information to third parties. You can opt out of analytics and marketing communications at any time. The full privacy policy is available at example.com/privacy."
        },
        {
            "question": "What is your shipping policy?",
            "answer": "We offer free standard shipping on all orders over $50. Standard shipping takes 3-5 business days. Express shipping (1-2 business days) is available for $12.99. Overnight shipping is available for $24.99 if ordered before 2 PM Eastern Time. We currently ship to the US and Canada only. All orders include tracking information sent via email once the package is dispatched."
        },

        # Additional Questions
        {
            "question": "Can I use my device internationally?",
            "answer": "Yes, our smartphones and tablets are unlocked and compatible with international networks. For optimal international use, we recommend checking your carrier's international plans or purchasing a local SIM card at your destination. Our devices support multiple bands for global connectivity."
        },
        {
            "question": "Do you offer trade-ins for old devices?",
            "answer": "Yes, we offer a trade-in program for qualifying devices. You can receive store credit or a discount on a new purchase depending on the model and condition of your device. To get an estimate, visit example.com/trade-in and enter your device information, or bring it to any of our retail locations for an in-person assessment."
        },
        {
            "question": "How do I apply for a job with your company?",
            "answer": "To apply for a job with our company, please visit our careers page at example.com/careers where you can browse open positions and submit your application. We update our job listings regularly and offer positions in retail, technical support, corporate offices, and remote work opportunities."
        }
    ]

    # Insert the data
    result = knowledge_base.insert_many(sample_data)

    print(f"Knowledge base created with {len(result.inserted_ids)} entries.")

create_chatbot_knowledge_base()