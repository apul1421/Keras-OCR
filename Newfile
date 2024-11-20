### **Framework Document for OCR Capabilities Using Generative AI for Underwriting Services (UWS)**  

---

### **1. Document Categorization**  
#### **a. Types of Verification**  
The following categories are established for document verification:  

1. **ID Verification**  
   - Documents confirming the identity of an individual.  
   - **Examples**: Passports, National ID cards, Driving licenses.  

2. **Address Verification**  
   - Documents confirming the residential address of an individual.  
   - **Examples**: Utility bills, Bank statements, Lease agreements.  

3. **Income Verification**  
   - Documents providing proof of income.  
   - **Examples**: Payslips, Tax returns, Bank statements.  

4. **Employment Verification**  
   - Documents confirming employment status and details.  
   - **Examples**: Employment letters, Contracts, Pay stubs.  

**Note**: A single document can belong to multiple categories.  

---

#### **b. Quality of Documents**  
Documents are classified based on their readability and format into the following categories:  

1. **Easy**  
   - Documents with a standard pre-existing format that are easy to read.  
   - **Examples**: Passports, Utility bills, Preformatted payslips.  

2. **Medium**  
   - Text-based documents that vary in format but are generally readable.  
   - **Examples**: Employment letters, Tax forms, Non-standardized contracts.  

3. **Hard**  
   - Poor-quality scans or documents with unexpected formats.  
   - **Examples**: Handwritten notes, Low-resolution or noisy scans.  

---

### **2. Measure of Success**  
#### **a. OCR Success Methodology**  
The success of the OCR system is evaluated using the following formula:  
\[
\text{Success Score} = \left( \frac{\text{Number of Correctly Extracted Fields}}{\text{Total Number of Fields}} \right) \times 100
\]  

**Threshold**:  
- A score above 80% is considered acceptable for fully automated processing.  
- Documents with a score below 80% require manual review.  

---

#### **b. RAG Metrics (Red, Amber, Green)**  
To classify document quality and OCR success:  
- **Green (High Confidence)**: Success Score ≥ 90%.  
  - Minimal errors, automated processing can proceed.  
- **Amber (Moderate Confidence)**: Success Score between 70%-89%.  
  - Some errors, needs partial manual intervention.  
- **Red (Low Confidence)**: Success Score < 70%.  
  - High errors, full manual review required.  

---

### **3. Stages of the Solution**  
The OCR framework provides the following solution stages:  

#### **a. Extraction**  
- The OCR tool extracts data from uploaded documents and structures it into a standardized tabular format.  
- **Example Output**:  
  | Field         | Extracted Value   | Confidence (%) |  
  |---------------|-------------------|----------------|  
  | Name          | John Doe          | 92%            |  
  | Date of Birth | 01/01/1990        | 88%            |  

#### **b. Summarization**  
- Extracted data is summarized in a standard format.  
- **Examples**:  
  - ID documents yield fields like Name and Date of Birth.  
  - Income documents yield fields like Annual Income and Employer Name.  

#### **c. Document Validation**  
- The tool runs extracted fields against validation rules.  
- **Examples of Validation**:  
  - Cross-check Name and Date of Birth against internal databases.  
  - Validate numerical formats (e.g., account numbers, tax IDs).  

#### **d. Analysis of Data**  
- **Policy-Driven Analysis**: Summarized data is analyzed against underwriting policies.  
- **Manual Review**: Documents requiring additional checks (e.g., ambiguous text or missing fields) are flagged for manual intervention.  

#### **e. Benchmarking**  
- A benchmarking template compares OCR outputs with other systems used in underwriting.  
- Metrics include extraction accuracy, processing time, and error rates.  

#### **f. Implementation**  
- The framework identifies document types that can be fully automated.  
- For documents with poor readability, a semi-automated workflow is recommended.  

---

### **4. Statistical Methods for Validation**  
To ensure high-quality OCR results, the following statistical methods are applied:  

1. **Field-Level Accuracy Analysis**  
   - Compare extracted text for each field with the expected format or ground truth.  
   - **Example**: Date of Birth must follow `DD/MM/YYYY`.  

2. **Confidence Thresholding**  
   - Assign weights to extracted fields based on OCR-provided confidence scores.  
   - Fields below a set threshold (e.g., 80%) are flagged.  

3. **String Matching Techniques**  
   - Use Levenshtein distance or cosine similarity to validate text similarity with known references.  

4. **Error Rate Calculation**  
   - Calculate the percentage of incorrect extractions relative to the total fields.  

5. **Pattern Recognition for Layouts**  
   - Validate document layouts against predefined templates using algorithms like Hidden Markov Models (HMMs) or Support Vector Machines (SVMs).  

---

### **5. Implementation Roadmap**  

#### **Step 1: Pilot Testing**  
- Test the OCR system on a sample of high-quality, medium-quality, and low-quality documents.  
- Measure performance metrics (accuracy, speed, manual effort required).  

#### **Step 2: Feedback Loop**  
- Analyze OCR errors to refine models.  
- Update validation rules based on real-world document variations.  

#### **Step 3: Full-Scale Deployment**  
- Implement the framework for all document types in underwriting workflows.  

#### **Step 4: Continuous Improvement**  
- Integrate machine learning algorithms to enhance OCR accuracy.  
- Regularly benchmark the system against competitors.  

---

### **6. Benchmarking Approach**  
- Compare the performance of the OCR framework with other OCR solutions (e.g., Google Vision, AWS Textract).  
- Evaluate the following metrics:  
  - **Extraction Accuracy**: Percentage of fields extracted correctly.  
  - **Processing Time**: Average time taken per document.  
  - **Error Rates**: Percentage of incorrect or missing fields.  

---

### **7. Benefits of the Framework**  
- **Automation**: Reduces manual effort and processing time.  
- **Scalability**: Handles high document volumes efficiently.  
- **Accuracy**: Ensures compliance with underwriting policies.  
- **Transparency**: Tracks OCR performance with measurable success metrics.  

This framework is designed to streamline document processing in underwriting services, ensuring a balance between automation, accuracy, and manual oversight where necessary.

### **Procedure for Rating the Quality of Documents**  

Document quality is critical for effective OCR performance. The following procedure ensures a systematic and objective evaluation of document quality based on predefined criteria:

---

### **Step 1: Define Quality Criteria**  

Documents are evaluated based on the following parameters:  
1. **Resolution**: Clarity of the image or scan (measured in DPI).  
2. **Format Consistency**: Adherence to expected templates or layouts.  
3. **Text Visibility**: Sharpness, font size, and readability of the text.  
4. **Noise/Artifacts**: Presence of marks, smudges, or unwanted lines.  
5. **Completeness**: Presence of all required fields (e.g., Name, Date).  
6. **Alignment**: Proper alignment (e.g., no tilting or skewing).  
7. **Language/Script**: Suitability of the language or script for OCR.  

---

### **Step 2: Assign Scoring Metrics for Each Criterion**  

Rate each parameter on a scale of **1-5**, where:  
- **5 (Excellent)**: Perfect condition, no issues.  
- **4 (Good)**: Minor issues that do not affect OCR performance.  
- **3 (Average)**: Noticeable issues that slightly impact OCR.  
- **2 (Poor)**: Significant issues requiring manual review.  
- **1 (Unusable)**: Document cannot be processed without major corrections.  

**Example Scoring Template**:  
| Parameter            | Score (1-5) | Notes                  |  
|-----------------------|-------------|------------------------|  
| Resolution            | 4           | Slightly blurred text. |  
| Format Consistency    | 5           | Perfect template.      |  
| Text Visibility       | 3           | Faint ink in sections. |  
| Noise/Artifacts       | 2           | Excessive marks.       |  
| Completeness          | 4           | One field missing.     |  
| Alignment             | 5           | Properly aligned.      |  
| Language/Script       | 5           | Supported language.    |  

---

### **Step 3: Calculate Overall Quality Score**  

Compute the overall quality score as a weighted average or simple average of all parameters:  
\[
\text{Quality Score} = \frac{\text{Sum of Parameter Scores}}{\text{Number of Parameters}}
\]  

For example, if the total score is 28 (out of a possible 35), the quality score is:  
\[
\text{Quality Score} = \frac{28}{35} \times 100 = 80\%
\]  

---

### **Step 4: Apply RAG (Red, Amber, Green) Ratings**  

Based on the overall quality score, classify the document into one of the following categories:  
- **Green (High Quality)**: Score ≥ 80%.  
  - OCR-ready with minimal issues.  
- **Amber (Moderate Quality)**: Score between 60-79%.  
  - OCR may work, but partial manual review may be required.  
- **Red (Low Quality)**: Score < 60%.  
  - OCR will likely fail; requires significant manual intervention or rescanning.  

---

### **Step 5: Automation Readiness Classification**  

After scoring, determine if the document can be processed automatically:  

| Rating | Action Required                  |  
|--------|----------------------------------|  
| Green  | Fully automated OCR processing.  |  
| Amber  | Semi-automated processing.       |  
| Red    | Manual review or document rescanning. |  

---

### **Step 6: Advanced Quality Validation Using Statistical Techniques**  

To make the quality rating more robust, apply the following statistical methods:  
1. **Text Sharpness**: Use edge-detection algorithms (e.g., Sobel, Canny) to measure sharpness.  
2. **Noise Detection**: Use entropy measures to identify unwanted noise.  
3. **Completeness Check**: Compare extracted fields against expected fields to identify gaps.  
4. **Skew Detection**: Use Hough Transform or Fourier Transform to detect and correct tilts.  

---

### **Step 7: Benchmarking Against Standards**  

Compare the rated document quality against a predefined quality benchmark for similar document types. For example:  
- Utility Bills: Expectation is high resolution with minimal noise.  
- Handwritten Notes: Expectation is low resolution and moderate noise.  

---

### **Step 8: Feedback Loop for Continuous Improvement**  

- Review documents flagged as Amber or Red and log recurring issues (e.g., frequent noise, misalignment).  
- Use the logged data to refine document preprocessing workflows (e.g., enhancing resolution or removing noise).  

---

This procedure ensures a structured and consistent way to assess and rate document quality, optimizing OCR performance in underwriting workflows.

### **Automatically Assigning Scores to Quality Criteria**  

Automating the scoring process involves leveraging image processing, machine learning, and statistical analysis techniques. Here’s how each quality criterion can be evaluated and scored programmatically:

---

### **1. Resolution (Clarity of the Document)**  
- **Method**:  
  - Use image metadata to determine DPI (dots per inch).  
  - Evaluate pixel sharpness using edge detection algorithms (e.g., Sobel or Canny edge detection).  
  - Compare the document resolution against predefined thresholds.  
    - **Thresholds**:  
      - DPI ≥ 300: Score = 5 (Excellent).  
      - DPI 200-299: Score = 4 (Good).  
      - DPI 150-199: Score = 3 (Average).  
      - DPI 100-149: Score = 2 (Poor).  
      - DPI < 100: Score = 1 (Unusable).  

---

### **2. Format Consistency**  
- **Method**:  
  - Train a template-matching model (e.g., OpenCV Template Matching or Structural Similarity Index Measure, SSIM) to compare document layout with a standard template.  
  - Evaluate alignment of key fields (e.g., name, date, address) using bounding boxes.  
  - **Thresholds**:  
    - SSIM ≥ 0.9: Score = 5.  
    - SSIM 0.8-0.89: Score = 4.  
    - SSIM 0.7-0.79: Score = 3.  
    - SSIM 0.6-0.69: Score = 2.  
    - SSIM < 0.6: Score = 1.  

---

### **3. Text Visibility (Sharpness and Readability)**  
- **Method**:  
  - Use contrast analysis to measure the difference between text and background.  
  - Use Optical Character Recognition (OCR) confidence scores provided by tools like Tesseract, AWS Textract, or Google Vision OCR.  
  - **Thresholds**:  
    - OCR Confidence ≥ 90%: Score = 5.  
    - OCR Confidence 80-89%: Score = 4.  
    - OCR Confidence 70-79%: Score = 3.  
    - OCR Confidence 60-69%: Score = 2.  
    - OCR Confidence < 60%: Score = 1.  

---

### **4. Noise/Artifacts (Unwanted Marks or Smudges)**  
- **Method**:  
  - Use entropy or histogram analysis to detect noise levels in the image.  
  - Apply filters like Gaussian blur or Median blur to estimate the amount of noise.  
  - **Thresholds**:  
    - Noise ≤ 5% of the document area: Score = 5.  
    - Noise 6%-10%: Score = 4.  
    - Noise 11%-20%: Score = 3.  
    - Noise 21%-30%: Score = 2.  
    - Noise > 30%: Score = 1.  

---

### **5. Completeness (Presence of All Required Fields)**  
- **Method**:  
  - Use key-value pair extraction models to identify and extract fields like Name, Address, and Date.  
  - Compare extracted fields with a predefined checklist of expected fields.  
  - **Thresholds**:  
    - All required fields present: Score = 5.  
    - One field missing: Score = 4.  
    - Two fields missing: Score = 3.  
    - Three fields missing: Score = 2.  
    - Four or more fields missing: Score = 1.  

---

### **6. Alignment (Document Tilt or Skew)**  
- **Method**:  
  - Use skew detection techniques like the Hough Transform or Fourier Transform to measure document tilt.  
  - Calculate the tilt angle and correct skew if required.  
  - **Thresholds**:  
    - Tilt Angle ≤ 1°: Score = 5.  
    - Tilt Angle 2°-3°: Score = 4.  
    - Tilt Angle 4°-5°: Score = 3.  
    - Tilt Angle 6°-10°: Score = 2.  
    - Tilt Angle > 10°: Score = 1.  

---

### **7. Language/Script Suitability**  
- **Method**:  
  - Use OCR-supported language lists to verify the compatibility of the document's language or script.  
  - **Thresholds**:  
    - Fully supported language: Score = 5.  
    - Partially supported (e.g., accents or diacritics missing): Score = 3.  
    - Unsupported language or script: Score = 1.  

---

### **Automated Workflow**  

1. **Preprocessing**:  
   - Normalize the image (e.g., resize, convert to grayscale, denoise).  

2. **Feature Extraction**:  
   - Extract document features using image processing tools (OpenCV, PIL) and OCR tools.  

3. **Apply Scoring Algorithms**:  
   - Use the thresholds defined above to calculate scores for each parameter.  

4. **Aggregate Scores**:  
   - Calculate the weighted or simple average of parameter scores:  
     \[
     \text{Overall Quality Score} = \frac{\text{Sum of Scores}}{\text{Number of Parameters}}
     \]  

5. **Quality Classification**:  
   - Assign RAG ratings (Green, Amber, Red) based on the overall score.  

---

### **Technology Stack for Automation**  

- **Image Processing**: OpenCV, PIL, Scikit-Image.  
- **OCR Engines**: Tesseract, AWS Textract, Google Vision OCR, or Microsoft Azure Computer Vision.  
- **Machine Learning Models**: TensorFlow, PyTorch for feature extraction and quality prediction.  
- **Programming Languages**: Python, Java, or any language compatible with OCR and ML libraries.  

---

### **Example Output**  

**Document Analysis Output**:  

| Parameter            | Score | Notes                              |  
|-----------------------|-------|------------------------------------|  
| Resolution            | 4     | Slightly blurry but readable.     |  
| Format Consistency    | 5     | Matches standard template.        |  
| Text Visibility       | 3     | Low contrast in some areas.       |  
| Noise/Artifacts       | 2     | Smudges detected on corners.      |  
| Completeness          | 4     | One minor field missing.          |  
| Alignment             | 5     | Properly aligned.                 |  
| Language/Script       | 5     | Fully supported language.         |  

**Overall Quality Score**:  
\[
\text{Overall Quality Score} = \frac{4 + 5 + 3 + 2 + 4 + 5 + 5}{7} = 4.0
\]  

**RAG Rating**: **Amber** (Moderate Quality).  

---

This procedure enables efficient, repeatable, and scalable scoring of document quality for OCR automation systems.
