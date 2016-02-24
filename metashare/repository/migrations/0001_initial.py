# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import metashare.repository.validators
import metashare.repository.fields
import django.core.exceptions
import django.db.models.deletion
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '__first__'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='actorInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Actor',
            },
        ),
        migrations.CreateModel(
            name='actualUseInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actualUse', models.CharField(help_text=b'Classification of the actual use of the resource', max_length=30, verbose_name=b'Actual use', choices=[('humanUse', 'Human Use'), ('nlpApplications', 'Nlp Applications')])),
                ('useNLPSpecific', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the NLP application for which the resource iscreated or the application in which it has actually been used.', max_length=22, verbose_name=b'Use nlpspecific', choices=[('parsing', 'Parsing'), ('contradictionDetection', 'Contradiction Detection'), ('opinionMining', 'Opinion Mining'), ('wordSenseDisambiguation', 'Word Sense Disambiguation'), ('voiceControl', 'Voice Control'), ('topicDetection_Tracking', 'Topic Detection_ Tracking'), ('textualEntailment', 'Textual Entailment'), ('textMining', 'Text Mining'), ('textCategorisation', 'Text Categorisation'), ('terminologyExtraction', 'Terminology Extraction'), ('summarisation', 'Summarisation'), ('spellChecking', 'Spell Checking'), ('speechUnderstanding', 'Speech Understanding'), ('speechToSpeechTranslation', 'Speech To Speech Translation'), ('speechSynthesis', 'Speech Synthesis'), ('speechRecognition', 'Speech Recognition'), ('signLanguageRecognition', 'Sign Language Recognition'), ('signLanguageGeneration', 'Sign Language Generation'), ('semanticWeb', 'Semantic Web'), ('questionAnswering', 'Question Answering'), ('informationExtraction', 'Information Extraction'), ('posTagging', 'Pos Tagging'), ('personIdentification', 'Person Identification'), ('naturalLanguageUnderstanding', 'Natural Language Understanding'), ('naturalLanguageGeneration', 'Natural Language Generation'), ('namedEntityRecognition', 'Named Entity Recognition'), ('multimediaDocumentProcessing', 'Multimedia Document Processing'), ('morphosyntacticTagging', 'Morphosyntactic Tagging'), ('morphologicalAnalysis', 'Morphological Analysis'), ('linguisticResearch', 'Linguistic Research'), ('lexiconEnhancement', 'Lexicon Enhancement'), ('lemmatization', 'Lemmatization'), ('languageModelsTraining', 'Language Models Training'), ('languageModelling', 'Language Modelling'), ('languageIdentification', 'Language Identification'), ('knowledgeRepresentation', 'Knowledge Representation'), ('knowledgeDiscovery', 'Knowledge Discovery'), ('emotionRecognition', 'Emotion Recognition'), ('emotionGeneration', 'Emotion Generation'), ('documentClassification', 'Document Classification'), ('derivationalMorphologicalAnalysis', 'Derivational Morphological Analysis'), ('coreferenceResolution', 'Coreference Resolution'), ('bilingualLexiconInduction', 'Bilingual Lexicon Induction'), ('annotation', 'Annotation'), ('webServices', 'Web Services'), ('eventExtraction', 'Event Extraction'), ('semanticRoleLabelling', 'Semantic Role Labelling'), ('readingAndWritingAidApplications', 'Reading And Writing Aid Applications'), ('temporalExpressionRecognition', 'Temporal Expression Recognition'), ('intra-documentCoreferenceResolution', 'Intra - Document Coreference Resolution'), ('visualSceneUnderstanding', 'Visual Scene Understanding'), ('entityMentionRecognition', 'Entity Mention Recognition'), ('sentimentAnalysis', 'Sentiment Analysis'), ('machineTranslation', 'Machine Translation'), ('persuasiveExpressionMining', 'Persuasive Expression Mining'), ('qualitativeAnalysis', 'Qualitative Analysis'), ('texToSpeechSynthesis', 'Tex To Speech Synthesis'), ('personRecognition', 'Person Recognition'), ('textGeneration', 'Text Generation'), ('avatarSynthesis', 'Avatar Synthesis'), ('discourseAnalysis', 'Discourse Analysis'), ('expressionRecognition', 'Expression Recognition'), ('faceRecognition', 'Face Recognition'), ('faceVerification', 'Face Verification'), ('humanoidAgentSynthesis', 'Humanoid Agent Synthesis'), ('informationRetrieval', 'Information Retrieval'), ('lexiconAccess', 'Lexicon Access'), ('lexiconAcquisitionFromCorpora', 'Lexicon Acquisition From Corpora'), ('lexiconExtractionFromLexica', 'Lexicon Extraction From Lexica'), ('lexiconFormatConversion', 'Lexicon Format Conversion'), ('lexiconMerging', 'Lexicon Merging'), ('lexiconVisualization', 'Lexicon Visualization'), ('lipTrackingAnalysis', 'Lip Tracking Analysis'), ('multimediaDevelopment', 'Multimedia Development'), ('speakerIdentification', 'Speaker Identification'), ('speakerVerification', 'Speaker Verification'), ('speechLipsCorrelationAnalysis', 'Speech Lips Correlation Analysis'), ('speechAnalysis', 'Speech Analysis'), ('speechAssistedVideoControl', 'Speech Assisted Video Control'), ('speechVerification', 'Speech Verification'), ('spokenDialogueSystems', 'Spoken Dialogue Systems'), ('talkingHeadSynthesis', 'Talking Head Synthesis'), ('userAuthentication', 'User Authentication'), ('other', 'Other')])),
                ('actualUseDetails', metashare.repository.fields.XmlCharField(help_text=b'Reports on the usage of the resource in free text', max_length=250, verbose_name=b'Actual use details', blank=True)),
            ],
            options={
                'verbose_name': 'Actual use',
            },
        ),
        migrations.CreateModel(
            name='annotationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annotationType', models.CharField(help_text=b'Specifies the annotation level of the resource or the annotation type a tool/ service requires or produces as an output', max_length=150, verbose_name=b'Annotation type', choices=[('alignment', 'Alignment'), ('discourseAnnotation', 'Discourse Annotation'), ('discourseAnnotation-audienceReactions', 'Discourse Annotation - Audience Reactions'), ('discourseAnnotation-coreference', 'Discourse Annotation - Coreference'), ('discourseAnnotation-dialogueActs', 'Discourse Annotation - Dialogue Acts'), ('discourseAnnotation-dialogueActs', 'Discourse Annotation - Dialogue Acts'), ('discourseAnnotation-discourseRelations', 'Discourse Annotation - Discourse Relations'), ('lemmatization', 'Lemmatization'), ('modalityAnnotation-bodyMovements', 'Modality Annotation - Body Movements'), ('modalityAnnotation-facialExpressions', 'Modality Annotation - Facial Expressions'), ('modalityAnnotation-gazeEyeMovements', 'Modality Annotation - Gaze Eye Movements'), ('modalityAnnotation-handArmGestures', 'Modality Annotation - Hand Arm Gestures'), ('modalityAnnotation-handManipulationOfObjects', 'Modality Annotation - Hand Manipulation Of Objects'), ('modalityAnnotation-headMovements', 'Modality Annotation - Head Movements'), ('modalityAnnotation-lipMovements', 'Modality Annotation - Lip Movements'), ('morphosyntacticAnnotation-bPosTagging', 'Morphosyntactic Annotation - B Pos Tagging'), ('morphosyntacticAnnotation-posTagging', 'Morphosyntactic Annotation - Pos Tagging'), ('other', 'Other'), ('segmentation', 'Segmentation'), ('semanticAnnotation', 'Semantic Annotation'), ('semanticAnnotation-certaintyLevel', 'Semantic Annotation - Certainty Level'), ('semanticAnnotation-emotions', 'Semantic Annotation - Emotions'), ('semanticAnnotation-emotions', 'Semantic Annotation - Emotions'), ('semanticAnnotation-entityMentions', 'Semantic Annotation - Entity Mentions'), ('semanticAnnotation-events', 'Semantic Annotation - Events'), ('semanticAnnotation-namedEntities', 'Semantic Annotation - Named Entities'), ('semanticAnnotation-polarity', 'Semantic Annotation - Polarity'), ('semanticAnnotation-questionTopicalTarget', 'Semantic Annotation - Question Topical Target'), ('semanticAnnotation-semanticClasses', 'Semantic Annotation - Semantic Classes'), ('semanticAnnotation-semanticRelations', 'Semantic Annotation - Semantic Relations'), ('semanticAnnotation-semanticRoles', 'Semantic Annotation - Semantic Roles'), ('semanticAnnotation-speechActs', 'Semantic Annotation - Speech Acts'), ('semanticAnnotation-temporalExpressions', 'Semantic Annotation - Temporal Expressions'), ('semanticAnnotation-textualEntailment', 'Semantic Annotation - Textual Entailment'), ('semanticAnnotation-wordSenses', 'Semantic Annotation - Word Senses'), ('speechAnnotation', 'Speech Annotation'), ('speechAnnotation', 'Speech Annotation'), ('speechAnnotation-orthographicTranscription', 'Speech Annotation - Orthographic Transcription'), ('speechAnnotation-paralanguageAnnotation', 'Speech Annotation - Paralanguage Annotation'), ('speechAnnotation-phoneticTranscription', 'Speech Annotation - Phonetic Transcription'), ('speechAnnotation-prosodicAnnotation', 'Speech Annotation - Prosodic Annotation'), ('speechAnnotation-soundEvents', 'Speech Annotation - Sound Events'), ('speechAnnotation-soundToTextAlignment', 'Speech Annotation - Sound To Text Alignment'), ('speechAnnotation-speakerIdentification', 'Speech Annotation - Speaker Identification'), ('speechAnnotation-speakerTurns', 'Speech Annotation - Speaker Turns'), ('stemming', 'Stemming'), ('structuralAnnotation', 'Structural Annotation'), ('syntacticAnnotation-shallowParsing', 'Syntactic Annotation - Shallow Parsing'), ('syntacticAnnotation-subcategorizationFrames', 'Syntactic Annotation - Subcategorization Frames'), ('syntacticAnnotation-treebanks', 'Syntactic Annotation - Treebanks'), ('syntacticosemanticAnnotation-links', 'Syntacticosemantic Annotation - Links'), ('translation', 'Translation'), ('transliteration', 'Transliteration')])),
                ('annotatedElements', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the elements annotated in each annotation level', max_length=2, verbose_name=b'Annotated elements', choices=[('speakerNoise', 'Speaker Noise'), ('backgroundNoise', 'Background Noise'), ('mispronunciations', 'Mispronunciations'), ('truncation', 'Truncation'), ('discourseMarkers', 'Discourse Markers'), ('other', 'Other')])),
                ('annotationStandoff', metashare.repository.fields.MetaBooleanField(help_text=b'Indicates whether the annotation is created inline or in a stand-off fashion', verbose_name=b'Annotation standoff', choices=[(True, b'Yes'), (False, b'No')])),
                ('segmentationLevel', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the segmentation unit in terms of which the resource has been segmented or the level of segmentation a tool/service requires/outputs', max_length=5, verbose_name=b'Segmentation level', choices=[('paragraph', 'Paragraph'), ('sentence', 'Sentence'), ('clause', 'Clause'), ('word', 'Word'), ('wordGroup', 'Word Group'), ('utterance', 'Utterance'), ('topic', 'Topic'), ('signal', 'Signal'), ('phoneme', 'Phoneme'), ('syllable', 'Syllable'), ('phrase', 'Phrase'), ('diphone', 'Diphone'), ('prosodicBoundaries', 'Prosodic Boundaries'), ('frame', 'Frame'), ('scene', 'Scene'), ('shot', 'Shot'), ('other', 'Other')])),
                ('annotationFormat', metashare.repository.fields.XmlCharField(help_text=b'Specifies the format that is used in the annotation process since often the mime type will not be sufficient for machine processing', max_length=100, verbose_name=b'Annotation format', blank=True)),
                ('tagset', metashare.repository.fields.XmlCharField(help_text=b'A name or a url reference to the tagset used in the annotation of the resource or used by the tool/service', max_length=500, verbose_name=b'Tagset', blank=True)),
                ('tagsetLanguageId', metashare.repository.fields.XmlCharField(help_text=b'The identifier of the tagset language; an autocompletion mechanism with values from the ISO 639 is provided in the editor, but the values can be subsequently edited for further specification (according to the IETF BCP47 guidelines)', max_length=20, verbose_name=b'Tagset language id', blank=True)),
                ('tagsetLanguageName', metashare.repository.fields.XmlCharField(help_text=b'The name of the tagset language; an autocompletion mechanism with values from the ISO 639 is provided in the editor, but the values can be subsequently edited for further specification (according to the IETF BCP47 guidelines)', max_length=100, verbose_name=b'Tagset language name', blank=True)),
                ('conformanceToStandardsBestPractices', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the standards or the best practices to which the tagset used for the annotation conforms', max_length=12, verbose_name=b'Conformance to standards best practices', choices=[('BLM', 'BLM'), ('CES', 'CES'), ('EAGLES', 'EAGLES'), ('EML', 'EML'), ('EMMA', 'EMMA'), ('GMX', 'GMX'), ('GrAF', 'GrAF'), ('HamNoSys', 'Ham No Sys'), ('InkML', 'InkML'), ('ISO12620', 'ISO12620'), ('ISO16642', 'ISO16642'), ('ISO1987', 'ISO1987'), ('ISO26162', 'ISO26162'), ('ISO30042', 'ISO30042'), ('ISO704', 'ISO704'), ('LMF', 'LMF'), ('MAF', 'MAF'), ('MLIF', 'MLIF'), ('MULTEXT', 'MULTEXT'), ('MUMIN', 'MUMIN'), ('multimodalInteractionFramework', 'Multimodal Interaction Framework'), ('OAXAL', 'OAXAL'), ('OWL', 'OWL'), ('pennTreeBank', 'Penn Tree Bank'), ('pragueTreebank', 'Prague Treebank'), ('RDF', 'RDF'), ('SemAF', 'SemAF'), ('SemAF_DA', 'SemAF_DA'), ('SemAF_NE', 'SemAF_NE'), ('SemAF_SRL', 'SemAF_SRL'), ('SemAF_DS', 'SemAF_DS'), ('SKOS', 'SKOS'), ('SRX', 'SRX'), ('SynAF', 'SynAF'), ('TBX', 'TBX'), ('TMX', 'TMX'), ('TEI', 'TEI'), ('TEI_P3', 'TEI_P3'), ('TEI_P4', 'TEI_P4'), ('TEI_P5', 'TEI_P5'), ('TimeML', 'TimeML'), ('XCES', 'XCES'), ('XLIFF', 'XLIFF'), ('WordNet', 'Word Net'), ('other', 'Other')])),
                ('theoreticModel', metashare.repository.fields.XmlCharField(help_text=b'Name of the theoretic model applied for the creation or enrichment of the resource, and/or a reference (URL or bibliographic reference) to informative material about the theoretic model used', max_length=500, verbose_name=b'Theoretic model', blank=True)),
                ('annotationMode', models.CharField(blank=True, help_text=b'Indicates whether the resource is annotated manually or by automatic processes', max_length=100, verbose_name=b'Annotation mode', choices=[('automatic', 'Automatic'), ('interactive', 'Interactive'), ('manual', 'Manual'), ('mixed', 'Mixed')])),
                ('annotationModeDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on annotation process', max_length=1000, verbose_name=b'Annotation mode details', blank=True)),
                ('annotationStartDate', models.DateField(help_text=b'The date in which the annotation process has started', null=True, verbose_name=b'Annotation start date', blank=True)),
                ('annotationEndDate', models.DateField(help_text=b'The date in which the annotation process has ended', null=True, verbose_name=b'Annotation end date', blank=True)),
                ('interannotatorAgreement', metashare.repository.fields.XmlCharField(help_text=b'Provides information on the interannotator agreement and the methods/metrics applied', max_length=1000, verbose_name=b'Interannotator agreement', blank=True)),
                ('intraannotatorAgreement', metashare.repository.fields.XmlCharField(help_text=b'Provides information on the intra-annotator agreement and the methods/metrics applied', max_length=1000, verbose_name=b'Intraannotator agreement', blank=True)),
            ],
            options={
                'verbose_name': 'Annotation',
            },
        ),
        migrations.CreateModel(
            name='audioClassificationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('audioGenre', models.CharField(help_text=b'A first indication of type of sounds recorded', max_length=30, verbose_name=b'Audio genre', choices=[('animalVocalizations', 'Animal Vocalizations'), ('humanNonSpeech', 'Human Non Speech'), ('instrumentalMusic', 'Instrumental Music'), ('noise', 'Noise'), ('other', 'Other'), ('song', 'Song'), ('speech', 'Speech')])),
                ('speechGenre', models.CharField(blank=True, help_text=b'The conventionalized discourse of the content of the resource, based on extra-linguistic and internal linguistic criteria; the values here are intended only for speech', max_length=30, verbose_name=b'Speech genre', choices=[('airTrafficControl', 'Air Traffic Control'), ('broadcastNews', 'Broadcast News'), ('call-in', 'Call - In'), ('conversation', 'Conversation'), ('debate', 'Debate'), ('emotionalExpressive', 'Emotional Expressive'), ('interview', 'Interview'), ('lecture', 'Lecture'), ('meeting', 'Meeting'), ('narrative', 'Narrative'), ('presentation', 'Presentation'), ('questionAnswer', 'Question Answer'), ('roundtable', 'Roundtable')])),
                ('subject_topic', metashare.repository.fields.XmlCharField(help_text=b'For corpora that have already been using subject classification', max_length=500, verbose_name=b'Subject topic', blank=True)),
                ('register', metashare.repository.fields.XmlCharField(help_text=b'For corpora that have already been using register classification', max_length=500, verbose_name=b'Register', blank=True)),
                ('conformanceToClassificationScheme', models.CharField(blank=True, help_text=b'Specifies the external classification schemes', max_length=100, verbose_name=b'Conformance to classification scheme', choices=[('ANC_domainClassification', 'ANC_domain Classification'), ('ANC_genreClassification', 'ANC_genre Classification'), ('BNC_domainClassification', 'BNC_domain Classification'), ('BNC_textTypeClassification', 'BNC_text Type Classification'), ('DDC_classification', 'DDC_classification'), ('libraryOfCongress_domainClassification', 'Library Of Congress_domain Classification'), ('libraryofCongressSubjectHeadings_classification', 'Libraryof Congress Subject Headings_classification'), ('MeSH_classification', 'MeSH_classification'), ('NLK_classification', 'NLK_classification'), ('other', 'Other'), ('PAROLE_genreClassification', 'PAROLE_genre Classification'), ('PAROLE_topicClassification', 'PAROLE_topic Classification'), ('UDC_classification', 'UDC_classification')])),
            ],
            options={
                'verbose_name': 'Audio classification',
            },
        ),
        migrations.CreateModel(
            name='audioContentInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speechItems', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the distinct elements that are pronounced and annotated as such', max_length=4, verbose_name=b'Speech items', choices=[('isolatedWords', 'Isolated Words'), ('isolatedDigits', 'Isolated Digits'), ('naturalNumbers', 'Natural Numbers'), ('properNouns', 'Proper Nouns'), ('applicationWords', 'Application Words'), ('phoneticallyRichSentences', 'Phonetically Rich Sentences'), ('phoneticallyRichWords', 'Phonetically Rich Words'), ('phoneticallyBalancedSentences', 'Phonetically Balanced Sentences'), ('moneyAmounts', 'Money Amounts'), ('creditCardNumbers', 'Credit Card Numbers'), ('telephoneNumbers', 'Telephone Numbers'), ('yesNoQuestions', 'Yes No Questions'), ('vcvSequences', 'Vcv Sequences'), ('freeSpeech', 'Free Speech'), ('other', 'Other')])),
                ('nonSpeechItems', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the distinct elements that maybe included in the audio corpus', max_length=2, verbose_name=b'Non speech items', choices=[('notes', 'Notes'), ('tempo', 'Tempo'), ('sounds', 'Sounds'), ('noise', 'Noise'), ('music', 'Music'), ('commercial ', 'Commercial'), ('other', 'Other')])),
                ('textualDescription', metashare.repository.fields.XmlCharField(help_text=b'The legend of the soundtrack', max_length=500, verbose_name=b'Textual description', blank=True)),
                ('noiseLevel', models.CharField(blank=True, help_text=b'Specifies the level of background noise', max_length=30, verbose_name=b'Noise level', choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')])),
            ],
            options={
                'verbose_name': 'Audio content',
            },
        ),
        migrations.CreateModel(
            name='audioFormatInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mimeType', metashare.repository.fields.XmlCharField(help_text=b'The mime-type of the resource which is a formalized specifier for the format included or a mime-type that the tool/service accepts; value to be taken from a subset of the official mime types of the Internet Assigned Numbers Authority (http://www.iana.org/)', max_length=50, verbose_name=b'Mime type')),
                ('signalEncoding', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the encoding the audio type uses', max_length=2, verbose_name=b'Signal encoding', choices=[('aLaw', 'A Law'), ('linearPCM', 'LinearPCM'), ('\xb5-law', '\u039c - Law'), ('ADPCM', 'ADPCM'), ('other', 'Other')])),
                ('samplingRate', models.BigIntegerField(help_text=b'Specifies the format of files contained in the resource in Hertz', null=True, verbose_name=b'Sampling rate', blank=True)),
                ('quantization', models.IntegerField(choices=[(8, 8), (16, 16), (24, 24), (32, 32), (64, 64)], max_length=1, blank=True, help_text=b'The number of bits for each audio sample', null=True, verbose_name=b'Quantization')),
                ('byteOrder', models.CharField(blank=True, help_text=b'The byte order of 2 or more bytes sample', max_length=30, verbose_name=b'Byte order', choices=[('bigEndian', 'Big Endian'), ('littleEndian', 'Little Endian')])),
                ('signConvention', models.CharField(blank=True, help_text=b'Binary representation of numbers', max_length=30, verbose_name=b'Sign convention', choices=[('floatingPoint', 'Floating Point'), ('signedInteger', 'Signed Integer'), ('unsignedInteger', 'Unsigned Integer')])),
                ('audioQualityMeasuresIncluded', models.CharField(blank=True, help_text=b'Specifies the audio quality measures', max_length=30, verbose_name=b'Audio quality measures included', choices=[('backgroundNoise', 'Background Noise'), ('clippingRate', 'Clipping Rate'), ('crossTalk', 'Cross Talk'), ('other', 'Other'), ('SNR', 'SNR')])),
                ('numberOfTracks', models.IntegerField(choices=[(1, 1), (2, 2), (4, 4), (8, 8)], max_length=1, blank=True, help_text=b'Specifies the number of audio channels', null=True, verbose_name=b'Number of tracks')),
                ('recordingQuality', models.CharField(blank=True, help_text=b'Indication of the audio or video recording quality', max_length=30, verbose_name=b'Recording quality', choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium'), ('veryHigh', 'Very High'), ('veryLow', 'Very Low')])),
            ],
            options={
                'verbose_name': 'Audio format',
            },
        ),
        migrations.CreateModel(
            name='audioSizeInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Audio size',
            },
        ),
        migrations.CreateModel(
            name='captureInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capturingDeviceType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The transducers through which the data is captured', max_length=4, verbose_name=b'Capturing device type', choices=[('studioEquipment', 'Studio Equipment'), ('microphone', 'Microphone'), ('closeTalkMicrophone', 'Close Talk Microphone'), ('farfieldMicrophone', 'Farfield Microphone'), ('lavalierMicrophone', 'Lavalier Microphone'), ('microphoneArray', 'Microphone Array'), ('embeddedMicrophone', 'Embedded Microphone'), ('largeMembraneMicrophone', 'Large Membrane Microphone'), ('laryngograph', 'Laryngograph'), ('telephoneFixed', 'Telephone Fixed'), ('telephoneMobile', 'Telephone Mobile'), ('telephoneIP', 'TelephoneIP'), ('camera', 'Camera'), ('webcam', 'Webcam'), ('other', 'Other')])),
                ('capturingDeviceTypeDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on the capturing device', max_length=400, verbose_name=b'Capturing device type details', blank=True)),
                ('capturingDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on the capturing method and procedure', max_length=400, verbose_name=b'Capturing details', blank=True)),
                ('capturingEnvironment', models.CharField(blank=True, help_text=b'Type of capturing environment', max_length=30, verbose_name=b'Capturing environment', choices=[('complex', 'Complex'), ('plain', 'Plain')])),
                ('sensorTechnology', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Specifies either the type of image sensor or the sensing method used in the camera or the image-capture device', max_length=200, verbose_name=b'Sensor technology', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('sceneIllumination', models.CharField(blank=True, help_text=b'Information on the illumination of the scene', max_length=30, verbose_name=b'Scene illumination', choices=[('daylight', 'Daylight'), ('fix', 'Fix'), ('multipleSources', 'Multiple Sources'), ('other', 'Other'), ('singleSource', 'Single Source'), ('variable', 'Variable')])),
            ],
            options={
                'verbose_name': 'Capture',
            },
        ),
        migrations.CreateModel(
            name='characterEncodingInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('characterEncoding', models.CharField(help_text=b'The name of the character encoding used in the resource or accepted by the tool/service', max_length=100, verbose_name=b'Character encoding', choices=[('Big5', 'Big5'), ('Big5-HKSCS', 'Big5 - HKSCS'), ('Big5_Solaris', 'Big5_ Solaris'), ('Cp037', 'Cp037'), ('Cp1006', 'Cp1006'), ('Cp1025', 'Cp1025'), ('Cp1026', 'Cp1026'), ('Cp1046', 'Cp1046'), ('Cp1047', 'Cp1047'), ('Cp1097', 'Cp1097'), ('Cp1098', 'Cp1098'), ('Cp1112', 'Cp1112'), ('Cp1122', 'Cp1122'), ('Cp1123', 'Cp1123'), ('Cp1124', 'Cp1124'), ('Cp1140', 'Cp1140'), ('Cp1141', 'Cp1141'), ('Cp1142', 'Cp1142'), ('Cp1143', 'Cp1143'), ('Cp1144', 'Cp1144'), ('Cp1145', 'Cp1145'), ('Cp1146', 'Cp1146'), ('Cp1147', 'Cp1147'), ('Cp1148', 'Cp1148'), ('Cp1149', 'Cp1149'), ('Cp1381', 'Cp1381'), ('Cp1383', 'Cp1383'), ('Cp273', 'Cp273'), ('Cp277', 'Cp277'), ('Cp278', 'Cp278'), ('Cp280', 'Cp280'), ('Cp284', 'Cp284'), ('Cp285', 'Cp285'), ('Cp297', 'Cp297'), ('Cp33722', 'Cp33722'), ('Cp420', 'Cp420'), ('Cp424', 'Cp424'), ('Cp437', 'Cp437'), ('Cp500', 'Cp500'), ('Cp737', 'Cp737'), ('Cp775', 'Cp775'), ('Cp838', 'Cp838'), ('Cp850', 'Cp850'), ('Cp852', 'Cp852'), ('Cp855', 'Cp855'), ('Cp856', 'Cp856'), ('Cp857', 'Cp857'), ('Cp858', 'Cp858'), ('Cp860', 'Cp860'), ('Cp861', 'Cp861'), ('Cp862', 'Cp862'), ('Cp863', 'Cp863'), ('Cp864', 'Cp864'), ('Cp865', 'Cp865'), ('Cp866', 'Cp866'), ('Cp868', 'Cp868'), ('Cp869', 'Cp869'), ('Cp870', 'Cp870'), ('Cp871', 'Cp871'), ('Cp874', 'Cp874'), ('Cp875', 'Cp875'), ('Cp918', 'Cp918'), ('Cp921', 'Cp921'), ('Cp922', 'Cp922'), ('Cp930', 'Cp930'), ('Cp933', 'Cp933'), ('Cp935', 'Cp935'), ('Cp937', 'Cp937'), ('Cp939', 'Cp939'), ('Cp942', 'Cp942'), ('Cp942C', 'Cp942C'), ('Cp943', 'Cp943'), ('Cp943C', 'Cp943C'), ('Cp948', 'Cp948'), ('Cp949', 'Cp949'), ('Cp949C', 'Cp949C'), ('Cp950', 'Cp950'), ('Cp964', 'Cp964'), ('Cp970', 'Cp970'), ('EUC-JP', 'EUC - JP'), ('EUC-KR', 'EUC - KR'), ('GB18030', 'GB18030'), ('GBK', 'GBK'), ('ISCII91', 'ISCII91'), ('ISO-2022-JP', 'ISO - 2022 - JP'), ('ISO-2022-KR', 'ISO - 2022 - KR'), ('ISO-8859-1', 'ISO - 8859 - 1'), ('ISO-8859-13', 'ISO - 8859 - 13'), ('ISO-8859-15', 'ISO - 8859 - 15'), ('ISO-8859-2', 'ISO - 8859 - 2'), ('ISO-8859-3', 'ISO - 8859 - 3'), ('ISO-8859-4', 'ISO - 8859 - 4'), ('ISO-8859-5', 'ISO - 8859 - 5'), ('ISO-8859-6', 'ISO - 8859 - 6'), ('ISO-8859-7', 'ISO - 8859 - 7'), ('ISO-8859-8', 'ISO - 8859 - 8'), ('ISO-8859-9', 'ISO - 8859 - 9'), ('ISO2022_CN_CNS', 'ISO2022_CN_CNS'), ('ISO2022_CN_GB', 'ISO2022_CN_GB'), ('JISAutoDetect', 'JIS Auto Detect'), ('KOI8-R', 'KOI8 - R'), ('MacArabic', 'Mac Arabic'), ('MacCentralEurope', 'Mac Central Europe'), ('MacCroatian', 'Mac Croatian'), ('MacCyrillic', 'Mac Cyrillic'), ('MacDingbat', 'Mac Dingbat'), ('MacGreek', 'Mac Greek'), ('MacHebrew', 'Mac Hebrew'), ('MacIceland', 'Mac Iceland'), ('MacRoman', 'Mac Roman'), ('MacRomania', 'Mac Romania'), ('MacSymbol', 'Mac Symbol'), ('MacThai', 'Mac Thai'), ('MacTurkish', 'Mac Turkish'), ('MacUkraine', 'Mac Ukraine'), ('MS874', 'MS874'), ('Shift_JIS', 'Shift_JIS'), ('TIS-620', 'TIS - 620'), ('US-ASCII', 'US - ASCII'), ('UTF-16', 'UTF - 16'), ('UTF-16BE', 'UTF - 16BE'), ('UTF-16LE', 'UTF - 16LE'), ('UTF-8', 'UTF - 8'), ('windows-1250', 'Windows - 1250'), ('windows-1251', 'Windows - 1251'), ('windows-1252', 'Windows - 1252'), ('windows-1253', 'Windows - 1253'), ('windows-1254', 'Windows - 1254'), ('windows-1255', 'Windows - 1255'), ('windows-1256', 'Windows - 1256'), ('windows-1257', 'Windows - 1257'), ('windows-1258', 'Windows - 1258'), ('windows-31j', 'Windows - 31j'), ('x-EUC-CN', 'X - EUC - CN'), ('x-EUC-JP-LINUX', 'X - EUC - JP - LINUX'), ('x-EUC-TW', 'X - EUC - TW'), ('x-MS950-HKSCS', 'X - MS950 - HKSCS'), ('x-mswin-936', 'X - Mswin - 936'), ('x-windows-949', 'X - Windows - 949'), ('x-windows-950', 'X - Windows - 950')])),
            ],
            options={
                'verbose_name': 'Character encoding',
            },
        ),
        migrations.CreateModel(
            name='communicationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', metashare.repository.fields.MultiTextField(help_text=b'The email address of a person or an organization', max_length=100, verbose_name=b'Email', validators=[django.core.validators.RegexValidator(b'^[^@]+@[^\\.]+\\..+(?!\\r?\\n)$', b'Not a valid emailAddress value.', django.core.exceptions.ValidationError)])),
                ('url', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A URL used as homepage of an entity (e.g. of a person, organization, resource etc.) and/or where an entity (e.g.LR, document etc.) is located', max_length=1000, verbose_name=b'Url', validators=[django.core.validators.RegexValidator(b"^(?i)((http|ftp)s?):\\/\\/(([a-z0-9.-]|%[0-9A-F]{2}){3,})(:(\\d+))?((\\/([a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(\\?(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(#(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(?!\\r?\\n)$", b'Not a valid URL value (must not contain non-ASCII characters, for example; see also RFC 2396).', django.core.exceptions.ValidationError)])),
                ('address', metashare.repository.fields.XmlCharField(help_text=b'The street and the number of the postal address of a person or organization', max_length=200, verbose_name=b'Address', blank=True)),
                ('zipCode', metashare.repository.fields.XmlCharField(help_text=b'The zip code of the postal address of a person or organization', max_length=30, verbose_name=b'Zip code', blank=True)),
                ('city', metashare.repository.fields.XmlCharField(help_text=b'The name of the city, town or village as mentioned in the postal address of a person or organization', max_length=50, verbose_name=b'City', blank=True)),
                ('region', metashare.repository.fields.XmlCharField(help_text=b'The name of the region, county or department as mentioned in the postal address of a person or organization', max_length=100, verbose_name=b'Region', blank=True)),
                ('country', metashare.repository.fields.XmlCharField(help_text=b'The name of the country mentioned in the postal address of a person or organization as defined in the list of values of ISO 3166', max_length=100, verbose_name=b'Country', blank=True)),
                ('telephoneNumber', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The telephone number of a person or an organization; recommended format: +_international code_city code_number', max_length=30, verbose_name=b'Telephone number', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('faxNumber', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The fax number of a person or an organization; recommended format: +_international code_city code_number', max_length=30, verbose_name=b'Fax number', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
            ],
            options={
                'verbose_name': 'Communication',
            },
        ),
        migrations.CreateModel(
            name='compressionInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compression', metashare.repository.fields.MetaBooleanField(help_text=b'Whether the audio, video or image is compressed or not', verbose_name=b'Compression', choices=[(True, b'Yes'), (False, b'No')])),
                ('compressionName', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The name of the compression applied', max_length=4, verbose_name=b'Compression name', choices=[('mpg', 'Mpg'), ('avi', 'Avi'), ('mov', 'Mov'), ('flac', 'Flac'), ('shorten', 'Shorten'), ('mp3', 'Mp3'), ('oggVorbis', 'Ogg Vorbis'), ('atrac', 'Atrac'), ('aac', 'Aac'), ('mpeg', 'Mpeg'), ('realAudio', 'Real Audio'), ('other', 'Other')])),
                ('compressionLoss', metashare.repository.fields.MetaBooleanField(help_text=b'Whether there is loss due to compression', verbose_name=b'Compression loss', choices=[(True, b'Yes'), (False, b'No')])),
            ],
            options={
                'verbose_name': 'Compression',
            },
        ),
        migrations.CreateModel(
            name='corpusAudioInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'audio', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('audioContentInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.audioContentInfoType_model', blank=True, help_text=b'Groups together information on the contents of the audio part of a resource', verbose_name=b'Audio content')),
                ('audioSizeInfo', models.ManyToManyField(help_text=b'SizeInfo Element for Audio parts of a resource', related_name='audioSizeInfo_corpusaudioinfotype_model_related', verbose_name=b'Audio size', to='repository.audioSizeInfoType_model')),
                ('captureInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.captureInfoType_model', blank=True, help_text=b'Groups together information on the capture of the audio or video part of a corpus', verbose_name=b'Capture')),
            ],
            options={
                'verbose_name': 'Corpus audio',
            },
        ),
        migrations.CreateModel(
            name='corpusImageInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'image', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('captureInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.captureInfoType_model', blank=True, help_text=b'Groups together information on the capture of the audio or video part of a corpus', verbose_name=b'Capture')),
            ],
            options={
                'verbose_name': 'Corpus image',
            },
        ),
        migrations.CreateModel(
            name='corpusMediaTypeType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corpusAudioInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.corpusAudioInfoType_model', blank=True, help_text=b'Groups together information on the audio module of a corpus', verbose_name=b'Corpus audio')),
                ('corpusImageInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.corpusImageInfoType_model', blank=True, help_text=b'Groups together information on the image component of a resource', verbose_name=b'Corpus image')),
            ],
            options={
                'verbose_name': 'Corpus media',
            },
        ),
        migrations.CreateModel(
            name='corpusTextInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'text', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('back_to_corpusmediatypetype_model', models.ForeignKey(blank=True, to='repository.corpusMediaTypeType_model', null=True)),
            ],
            options={
                'verbose_name': 'Corpus text',
            },
        ),
        migrations.CreateModel(
            name='corpusTextNgramInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'textNgram', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
            ],
            options={
                'verbose_name': 'Corpus text ngram',
            },
        ),
        migrations.CreateModel(
            name='corpusTextNumericalInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'textNumerical', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('captureInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.captureInfoType_model', blank=True, help_text=b'Groups together information on the capture of the audio or video part of a corpus', verbose_name=b'Capture')),
            ],
            options={
                'verbose_name': 'Corpus text numerical',
            },
        ),
        migrations.CreateModel(
            name='corpusVideoInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'video', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('back_to_corpusmediatypetype_model', models.ForeignKey(blank=True, to='repository.corpusMediaTypeType_model', null=True)),
                ('captureInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.captureInfoType_model', blank=True, help_text=b'Groups together information on the capture of the audio or video part of a corpus', verbose_name=b'Capture')),
            ],
            options={
                'verbose_name': 'Corpus video',
            },
        ),
        migrations.CreateModel(
            name='creationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creationMode', models.CharField(blank=True, help_text=b'Specifies whether the resource is created automatically or in a manual or interactive mode', max_length=30, verbose_name=b'Creation mode', choices=[('automatic', 'Automatic'), ('interactive', 'Interactive'), ('manual', 'Manual'), ('mixed', 'Mixed')])),
                ('creationModeDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on the creation methods and processes', max_length=200, verbose_name=b'Creation mode details', blank=True)),
            ],
            options={
                'verbose_name': 'Creation',
            },
        ),
        migrations.CreateModel(
            name='distributionInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('availability', models.CharField(help_text=b'Specifies the availability status of the resource; restrictionsOfUse can be further used to indicate the specific terms of availability', max_length=40, verbose_name=b'Availability', choices=[('available-restrictedUse', 'Available - Restricted Use'), ('available-unrestrictedUse', 'Available - Unrestricted Use'), ('notAvailableThroughMetaShare', 'Not Available Through Meta Share'), ('underNegotiation', 'Under Negotiation')])),
                ('availabilityEndDate', models.DateField(help_text=b'Specifies the end date of availability of a resource - only for cases where a resource is available for a restricted time period.', null=True, verbose_name=b'Availability end date', blank=True)),
                ('availabilityStartDate', models.DateField(help_text=b'Specifies the start date of availability of a resource - only for cases where a resource is available for a restricted time period.', null=True, verbose_name=b'Availability start date', blank=True)),
            ],
            options={
                'verbose_name': 'Distribution',
            },
        ),
        migrations.CreateModel(
            name='documentationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Documentation',
            },
        ),
        migrations.CreateModel(
            name='documentListType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Document list',
            },
        ),
        migrations.CreateModel(
            name='domainInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', metashare.repository.fields.XmlCharField(help_text=b'Specifies the application domain of the resource or the tool/service', max_length=100, verbose_name=b'Domain')),
                ('conformanceToClassificationScheme', models.CharField(blank=True, help_text=b'Specifies the external classification schemes', max_length=100, verbose_name=b'Conformance to classification scheme', choices=[('ANC_domainClassification', 'ANC_domain Classification'), ('ANC_genreClassification', 'ANC_genre Classification'), ('BNC_domainClassification', 'BNC_domain Classification'), ('BNC_textTypeClassification', 'BNC_text Type Classification'), ('DDC_classification', 'DDC_classification'), ('libraryOfCongress_domainClassification', 'Library Of Congress_domain Classification'), ('libraryofCongressSubjectHeadings_classification', 'Libraryof Congress Subject Headings_classification'), ('MeSH_classification', 'MeSH_classification'), ('NLK_classification', 'NLK_classification'), ('other', 'Other'), ('PAROLE_genreClassification', 'PAROLE_genre Classification'), ('PAROLE_topicClassification', 'PAROLE_topic Classification'), ('UDC_classification', 'UDC_classification')])),
                ('back_to_corpusaudioinfotype_model', models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True)),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextngraminfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True)),
                ('back_to_corpusvideoinfotype_model', models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Domain',
            },
        ),
        migrations.CreateModel(
            name='durationOfAudioInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.BigIntegerField(help_text=b'Specifies the size of the resource with regard to the SizeUnit measurement in form of a number', verbose_name=b'Size')),
                ('durationUnit', models.CharField(help_text=b'Specification of the unit of size that is used when providing information on the size of a resource', max_length=30, verbose_name=b'Duration unit', choices=[('hours', 'Hours'), ('minutes', 'Minutes'), ('seconds', 'Seconds')])),
                ('back_to_audiosizeinfotype_model', models.ForeignKey(blank=True, to='repository.audioSizeInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Duration of audio',
            },
        ),
        migrations.CreateModel(
            name='durationOfEffectiveSpeechInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.BigIntegerField(help_text=b'Specifies the size of the resource with regard to the SizeUnit measurement in form of a number', verbose_name=b'Size')),
                ('durationUnit', models.CharField(help_text=b'Specification of the unit of size that is used when providing information on the size of a resource', max_length=30, verbose_name=b'Duration unit', choices=[('hours', 'Hours'), ('minutes', 'Minutes'), ('seconds', 'Seconds')])),
                ('back_to_audiosizeinfotype_model', models.ForeignKey(blank=True, to='repository.audioSizeInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Duration of effective speech',
            },
        ),
        migrations.CreateModel(
            name='dynamicElementInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfElement', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The type of objects or people that represented in the video or image part of the resource', max_length=1000, verbose_name=b'Type of element', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('bodyParts', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The body parts visible in the video or image part of the resource', max_length=3, verbose_name=b'Body parts', choices=[('arms', 'Arms'), ('face', 'Face'), ('feet', 'Feet'), ('hands', 'Hands'), ('head', 'Head'), ('legs', 'Legs'), ('mouth', 'Mouth'), ('wholeBody', 'Whole Body'), ('none', 'None')])),
                ('distractors', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Any distractors visible in the resource', max_length=1000, verbose_name=b'Distractors', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('interactiveMedia', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Any interactive media visible in the resource', max_length=1000, verbose_name=b'Interactive media', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('faceViews', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the view of the face(s) that appear in the video or on the image part of the resource', max_length=1000, verbose_name=b'Face views', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('faceExpressions', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the facial expressions visible in the resource', max_length=1000, verbose_name=b'Face expressions', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('bodyMovement', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the body parts that move in the video part of the resource', max_length=1000, verbose_name=b'Body movement', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('gestures', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the type of gestures visible in the resource', max_length=1000, verbose_name=b'Gestures', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('handArmMovement', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the movement of hands and/or arms visible in the resource', max_length=1000, verbose_name=b'Hand arm movement', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('handManipulation', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Gives information on the manipulation of objects by hand', max_length=1000, verbose_name=b'Hand manipulation', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('headMovement', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the movements of the head visible in the resource', max_length=1000, verbose_name=b'Head movement', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('eyeMovement', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the movement of the eyes visible in the resource', max_length=1000, verbose_name=b'Eye movement', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('posesPerSubject', models.IntegerField(help_text=b'The number of poses per subject that participates in the video part of the resource', null=True, verbose_name=b'Poses per subject', blank=True)),
            ],
            options={
                'verbose_name': 'Dynamic element',
            },
        ),
        migrations.CreateModel(
            name='foreseenUseInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foreseenUse', models.CharField(help_text=b'Classification of the intended use of the resource', max_length=30, verbose_name=b'Foreseen use', choices=[('humanUse', 'Human Use'), ('nlpApplications', 'Nlp Applications')])),
                ('useNLPSpecific', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the NLP application for which the resource iscreated or the application in which it has actually been used.', max_length=22, verbose_name=b'Use nlpspecific', choices=[('parsing', 'Parsing'), ('contradictionDetection', 'Contradiction Detection'), ('opinionMining', 'Opinion Mining'), ('wordSenseDisambiguation', 'Word Sense Disambiguation'), ('voiceControl', 'Voice Control'), ('topicDetection_Tracking', 'Topic Detection_ Tracking'), ('textualEntailment', 'Textual Entailment'), ('textMining', 'Text Mining'), ('textCategorisation', 'Text Categorisation'), ('terminologyExtraction', 'Terminology Extraction'), ('summarisation', 'Summarisation'), ('spellChecking', 'Spell Checking'), ('speechUnderstanding', 'Speech Understanding'), ('speechToSpeechTranslation', 'Speech To Speech Translation'), ('speechSynthesis', 'Speech Synthesis'), ('speechRecognition', 'Speech Recognition'), ('signLanguageRecognition', 'Sign Language Recognition'), ('signLanguageGeneration', 'Sign Language Generation'), ('semanticWeb', 'Semantic Web'), ('questionAnswering', 'Question Answering'), ('informationExtraction', 'Information Extraction'), ('posTagging', 'Pos Tagging'), ('personIdentification', 'Person Identification'), ('naturalLanguageUnderstanding', 'Natural Language Understanding'), ('naturalLanguageGeneration', 'Natural Language Generation'), ('namedEntityRecognition', 'Named Entity Recognition'), ('multimediaDocumentProcessing', 'Multimedia Document Processing'), ('morphosyntacticTagging', 'Morphosyntactic Tagging'), ('morphologicalAnalysis', 'Morphological Analysis'), ('linguisticResearch', 'Linguistic Research'), ('lexiconEnhancement', 'Lexicon Enhancement'), ('lemmatization', 'Lemmatization'), ('languageModelsTraining', 'Language Models Training'), ('languageModelling', 'Language Modelling'), ('languageIdentification', 'Language Identification'), ('knowledgeRepresentation', 'Knowledge Representation'), ('knowledgeDiscovery', 'Knowledge Discovery'), ('emotionRecognition', 'Emotion Recognition'), ('emotionGeneration', 'Emotion Generation'), ('documentClassification', 'Document Classification'), ('derivationalMorphologicalAnalysis', 'Derivational Morphological Analysis'), ('coreferenceResolution', 'Coreference Resolution'), ('bilingualLexiconInduction', 'Bilingual Lexicon Induction'), ('annotation', 'Annotation'), ('webServices', 'Web Services'), ('eventExtraction', 'Event Extraction'), ('semanticRoleLabelling', 'Semantic Role Labelling'), ('readingAndWritingAidApplications', 'Reading And Writing Aid Applications'), ('temporalExpressionRecognition', 'Temporal Expression Recognition'), ('intra-documentCoreferenceResolution', 'Intra - Document Coreference Resolution'), ('visualSceneUnderstanding', 'Visual Scene Understanding'), ('entityMentionRecognition', 'Entity Mention Recognition'), ('sentimentAnalysis', 'Sentiment Analysis'), ('machineTranslation', 'Machine Translation'), ('persuasiveExpressionMining', 'Persuasive Expression Mining'), ('qualitativeAnalysis', 'Qualitative Analysis'), ('texToSpeechSynthesis', 'Tex To Speech Synthesis'), ('personRecognition', 'Person Recognition'), ('textGeneration', 'Text Generation'), ('avatarSynthesis', 'Avatar Synthesis'), ('discourseAnalysis', 'Discourse Analysis'), ('expressionRecognition', 'Expression Recognition'), ('faceRecognition', 'Face Recognition'), ('faceVerification', 'Face Verification'), ('humanoidAgentSynthesis', 'Humanoid Agent Synthesis'), ('informationRetrieval', 'Information Retrieval'), ('lexiconAccess', 'Lexicon Access'), ('lexiconAcquisitionFromCorpora', 'Lexicon Acquisition From Corpora'), ('lexiconExtractionFromLexica', 'Lexicon Extraction From Lexica'), ('lexiconFormatConversion', 'Lexicon Format Conversion'), ('lexiconMerging', 'Lexicon Merging'), ('lexiconVisualization', 'Lexicon Visualization'), ('lipTrackingAnalysis', 'Lip Tracking Analysis'), ('multimediaDevelopment', 'Multimedia Development'), ('speakerIdentification', 'Speaker Identification'), ('speakerVerification', 'Speaker Verification'), ('speechLipsCorrelationAnalysis', 'Speech Lips Correlation Analysis'), ('speechAnalysis', 'Speech Analysis'), ('speechAssistedVideoControl', 'Speech Assisted Video Control'), ('speechVerification', 'Speech Verification'), ('spokenDialogueSystems', 'Spoken Dialogue Systems'), ('talkingHeadSynthesis', 'Talking Head Synthesis'), ('userAuthentication', 'User Authentication'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Foreseen use',
            },
        ),
        migrations.CreateModel(
            name='geographicCoverageInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geographicCoverage', metashare.repository.fields.XmlCharField(help_text=b'The geographic region that the content of a resource is about; for countries, recommended use of ISO-3166', max_length=100, verbose_name=b'Geographic coverage')),
                ('back_to_corpusaudioinfotype_model', models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True)),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextngraminfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True)),
                ('back_to_corpusvideoinfotype_model', models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Geographic coverage',
            },
        ),
        migrations.CreateModel(
            name='identificationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resourceName', metashare.repository.fields.DictField(help_text=b'The full name by which the resource is known; the element can be repeated for the different language versions using the "lang" attribute to specify the language.', null=True, verbose_name=b'Resource name', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('description', metashare.repository.fields.DictField(help_text=b'Provides the description of the resource in prose; the element can be repeated for the different language versions using the "lang" attribute to specify the language.', null=True, verbose_name=b'Description', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('resourceShortName', metashare.repository.fields.DictField(blank=True, help_text=b'The short form (abbreviation, acronym etc.) used to identify the resource; the element can be repeated for the different language versions using the "lang" attribute to specify the language.', null=True, verbose_name=b'Resource short name', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('url', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A URL used as homepage of an entity (e.g. of a person, organization, resource etc.) and/or where an entity (e.g.LR, document etc.) is located', max_length=1000, verbose_name=b'Url', validators=[django.core.validators.RegexValidator(b"^(?i)((http|ftp)s?):\\/\\/(([a-z0-9.-]|%[0-9A-F]{2}){3,})(:(\\d+))?((\\/([a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(\\?(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(#(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(?!\\r?\\n)$", b'Not a valid URL value (must not contain non-ASCII characters, for example; see also RFC 2396).', django.core.exceptions.ValidationError)])),
                ('metaShareId', metashare.repository.fields.XmlCharField(default=b'NOT_DEFINED_FOR_V2', help_text=b'An unambiguous referent to the resource within META-SHARE; it reflects to the unique system id provided automatically by the MetaShare software', max_length=100, verbose_name=b'Meta share id')),
                ('identifier', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A reference to the resource like a pid or an internal identifier used by the resource provider', max_length=100, verbose_name=b'Identifier', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
            ],
            options={
                'verbose_name': 'Identification',
            },
        ),
        migrations.CreateModel(
            name='imageClassificationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imageGenre', metashare.repository.fields.XmlCharField(help_text=b'A first indication of the genre of images', max_length=1000, verbose_name=b'Image genre', blank=True)),
                ('subject_topic', metashare.repository.fields.XmlCharField(help_text=b'For corpora that have already been using subject classification', max_length=1000, verbose_name=b'Subject topic', blank=True)),
                ('conformanceToClassificationScheme', models.CharField(blank=True, help_text=b'Specifies the external classification schemes', max_length=100, verbose_name=b'Conformance to classification scheme', choices=[('ANC_domainClassification', 'ANC_domain Classification'), ('ANC_genreClassification', 'ANC_genre Classification'), ('BNC_domainClassification', 'BNC_domain Classification'), ('BNC_textTypeClassification', 'BNC_text Type Classification'), ('DDC_classification', 'DDC_classification'), ('libraryOfCongress_domainClassification', 'Library Of Congress_domain Classification'), ('libraryofCongressSubjectHeadings_classification', 'Libraryof Congress Subject Headings_classification'), ('MeSH_classification', 'MeSH_classification'), ('NLK_classification', 'NLK_classification'), ('other', 'Other'), ('PAROLE_genreClassification', 'PAROLE_genre Classification'), ('PAROLE_topicClassification', 'PAROLE_topic Classification'), ('UDC_classification', 'UDC_classification')])),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Image classification',
            },
        ),
        migrations.CreateModel(
            name='imageContentInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfImageContent', metashare.repository.fields.MultiTextField(help_text=b'The main types of object or people represented in the image corpus', max_length=1000, verbose_name=b'Type of image content', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('textIncludedInImage', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Provides information on the type of text that may be on the image', max_length=2, verbose_name=b'Text included in image', choices=[('captions', 'Captions'), ('subtitles', 'Subtitles'), ('captureTime', 'Capture Time'), ('none', 'None')])),
            ],
            options={
                'verbose_name': 'Image content',
            },
        ),
        migrations.CreateModel(
            name='imageFormatInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mimeType', metashare.repository.fields.XmlCharField(help_text=b'The mime-type of the resource which is a formalized specifier for the format included or a mime-type that the tool/service accepts; value to be taken from a subset of the official mime types of the Internet Assigned Numbers Authority (http://www.iana.org/)', max_length=50, verbose_name=b'Mime type')),
                ('colourSpace', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Defines the colour space for the video', max_length=2, verbose_name=b'Colour space', choices=[('RGB', 'RGB'), ('CMYK', 'CMYK'), ('4:2:2', '4:2:2'), ('YUV', 'YUV')])),
                ('colourDepth', models.IntegerField(help_text=b'The number of bits used to represent the colour of a single pixel', null=True, verbose_name=b'Colour depth', blank=True)),
                ('visualModelling', models.CharField(blank=True, help_text=b'The dimensional form applied on video or image corpus', max_length=30, verbose_name=b'Visual modelling', choices=[('2D', '2D'), ('3D', '3D')])),
                ('rasterOrVectorGraphics', models.CharField(blank=True, help_text=b'Indicates if the image is stored as raster or vector graphics', max_length=30, verbose_name=b'Raster or vector graphics', choices=[('raster', 'Raster'), ('vector', 'Vector')])),
                ('quality', models.CharField(blank=True, help_text=b'Specifies the quality level of image resource', max_length=30, verbose_name=b'Quality', choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium'), ('veryHigh', 'Very High'), ('veryLow', 'Very Low')])),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Image format',
            },
        ),
        migrations.CreateModel(
            name='inputInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.MultiSelectField(help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=2, verbose_name=b'Media type', choices=[('text', 'Text'), ('audio', 'Audio'), ('video', 'Video'), ('image', 'Image'), ('textNumerical', 'Text Numerical')])),
                ('resourceType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The type of the resource that a tool or service takes as input or produces as output', max_length=1, verbose_name=b'Resource type', choices=[('corpus', 'Corpus'), ('lexicalConceptualResource', 'Lexical Conceptual Resource'), ('languageDescription', 'Language Description')])),
                ('modalityType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the type of the modality represented in the resource or processed by a tool/service', max_length=3, verbose_name=b'Modality type', choices=[('bodyGesture', 'Body Gesture'), ('facialExpression', 'Facial Expression'), ('voice', 'Voice'), ('combinationOfModalities', 'Combination Of Modalities'), ('signLanguage', 'Sign Language'), ('spokenLanguage', 'Spoken Language'), ('writtenLanguage', 'Written Language'), ('other', 'Other')])),
                ('languageName', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A human understandable name of the language that is used in the resource or supported by the tool/service according to the IETF BCP47 standard', max_length=100, verbose_name=b'Language name', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('languageId', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The identifier of the language that is included in the resource or supported by the tool/service according to the IETF BCP47 standard', max_length=100, verbose_name=b'Language id', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('languageVarietyName', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Specifies the type of the language variety that occurs in the resource or is supported by a tool/service', max_length=100, verbose_name=b'Language variety name', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('mimeType', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The mime-type of the resource which is a formalized specifier for the format included or a mime-type that the tool/service accepts; value to be taken from a subset of the official mime types of the Internet Assigned Numbers Authority (http://www.iana.org/)', max_length=50, verbose_name=b'Mime type', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('characterEncoding', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The name of the character encoding used in the resource or accepted by the tool/service', max_length=36, verbose_name=b'Character encoding', choices=[('US-ASCII', 'US - ASCII'), ('windows-1250', 'Windows - 1250'), ('windows-1251', 'Windows - 1251'), ('windows-1252', 'Windows - 1252'), ('windows-1253', 'Windows - 1253'), ('windows-1254', 'Windows - 1254'), ('windows-1257', 'Windows - 1257'), ('ISO-8859-1', 'ISO - 8859 - 1'), ('ISO-8859-2', 'ISO - 8859 - 2'), ('ISO-8859-4', 'ISO - 8859 - 4'), ('ISO-8859-5', 'ISO - 8859 - 5'), ('ISO-8859-7', 'ISO - 8859 - 7'), ('ISO-8859-9', 'ISO - 8859 - 9'), ('ISO-8859-13', 'ISO - 8859 - 13'), ('ISO-8859-15', 'ISO - 8859 - 15'), ('KOI8-R', 'KOI8 - R'), ('UTF-8', 'UTF - 8'), ('UTF-16', 'UTF - 16'), ('UTF-16BE', 'UTF - 16BE'), ('UTF-16LE', 'UTF - 16LE'), ('windows-1255', 'Windows - 1255'), ('windows-1256', 'Windows - 1256'), ('windows-1258', 'Windows - 1258'), ('ISO-8859-3', 'ISO - 8859 - 3'), ('ISO-8859-6', 'ISO - 8859 - 6'), ('ISO-8859-8', 'ISO - 8859 - 8'), ('windows-31j', 'Windows - 31j'), ('EUC-JP', 'EUC - JP'), ('x-EUC-JP-LINUX', 'X - EUC - JP - LINUX'), ('Shift_JIS', 'Shift_JIS'), ('ISO-2022-JP', 'ISO - 2022 - JP'), ('x-mswin-936', 'X - Mswin - 936'), ('GB18030', 'GB18030'), ('x-EUC-CN', 'X - EUC - CN'), ('GBK', 'GBK'), ('ISCII91', 'ISCII91'), ('x-windows-949', 'X - Windows - 949'), ('EUC-KR', 'EUC - KR'), ('ISO-2022-KR', 'ISO - 2022 - KR'), ('x-windows-950', 'X - Windows - 950'), ('x-MS950-HKSCS', 'X - MS950 - HKSCS'), ('x-EUC-TW', 'X - EUC - TW'), ('Big5', 'Big5'), ('Big5-HKSCS', 'Big5 - HKSCS'), ('TIS-620', 'TIS - 620'), ('Big5_Solaris', 'Big5_ Solaris'), ('Cp037', 'Cp037'), ('Cp273', 'Cp273'), ('Cp277', 'Cp277'), ('Cp278', 'Cp278'), ('Cp280', 'Cp280'), ('Cp284', 'Cp284'), ('Cp285', 'Cp285'), ('Cp297', 'Cp297'), ('Cp420', 'Cp420'), ('Cp424', 'Cp424'), ('Cp437', 'Cp437'), ('Cp500', 'Cp500'), ('Cp737', 'Cp737'), ('Cp775', 'Cp775'), ('Cp838', 'Cp838'), ('Cp850', 'Cp850'), ('Cp852', 'Cp852'), ('Cp855', 'Cp855'), ('Cp856', 'Cp856'), ('Cp857', 'Cp857'), ('Cp858', 'Cp858'), ('Cp860', 'Cp860'), ('Cp861', 'Cp861'), ('Cp862', 'Cp862'), ('Cp863', 'Cp863'), ('Cp864', 'Cp864'), ('Cp865', 'Cp865'), ('Cp866', 'Cp866'), ('Cp868', 'Cp868'), ('Cp869', 'Cp869'), ('Cp870', 'Cp870'), ('Cp871', 'Cp871'), ('Cp874', 'Cp874'), ('Cp875', 'Cp875'), ('Cp918', 'Cp918'), ('Cp921', 'Cp921'), ('Cp922', 'Cp922'), ('Cp930', 'Cp930'), ('Cp933', 'Cp933'), ('Cp935', 'Cp935'), ('Cp937', 'Cp937'), ('Cp939', 'Cp939'), ('Cp942', 'Cp942'), ('Cp942C', 'Cp942C'), ('Cp943', 'Cp943'), ('Cp943C', 'Cp943C'), ('Cp948', 'Cp948'), ('Cp949', 'Cp949'), ('Cp949C', 'Cp949C'), ('Cp950', 'Cp950'), ('Cp964', 'Cp964'), ('Cp970', 'Cp970'), ('Cp1006', 'Cp1006'), ('Cp1025', 'Cp1025'), ('Cp1026', 'Cp1026'), ('Cp1046', 'Cp1046'), ('Cp1047', 'Cp1047'), ('Cp1097', 'Cp1097'), ('Cp1098', 'Cp1098'), ('Cp1112', 'Cp1112'), ('Cp1122', 'Cp1122'), ('Cp1123', 'Cp1123'), ('Cp1124', 'Cp1124'), ('Cp1140', 'Cp1140'), ('Cp1141', 'Cp1141'), ('Cp1142', 'Cp1142'), ('Cp1143', 'Cp1143'), ('Cp1144', 'Cp1144'), ('Cp1145', 'Cp1145'), ('Cp1146', 'Cp1146'), ('Cp1147', 'Cp1147'), ('Cp1148', 'Cp1148'), ('Cp1149', 'Cp1149'), ('Cp1381', 'Cp1381'), ('Cp1383', 'Cp1383'), ('Cp33722', 'Cp33722'), ('ISO2022_CN_CNS', 'ISO2022_CN_CNS'), ('ISO2022_CN_GB', 'ISO2022_CN_GB'), ('JISAutoDetect', 'JIS Auto Detect'), ('MS874', 'MS874'), ('MacArabic', 'Mac Arabic'), ('MacCentralEurope', 'Mac Central Europe'), ('MacCroatian', 'Mac Croatian'), ('MacCyrillic', 'Mac Cyrillic'), ('MacDingbat', 'Mac Dingbat'), ('MacGreek', 'Mac Greek'), ('MacHebrew', 'Mac Hebrew'), ('MacIceland', 'Mac Iceland'), ('MacRoman', 'Mac Roman'), ('MacRomania', 'Mac Romania'), ('MacSymbol', 'Mac Symbol'), ('MacThai', 'Mac Thai'), ('MacTurkish', 'Mac Turkish'), ('MacUkraine', 'Mac Ukraine')])),
                ('annotationType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the annotation level of the resource or the annotation type a tool/ service requires or produces as an output', max_length=14, verbose_name=b'Annotation type', choices=[('alignment', 'Alignment'), ('discourseAnnotation', 'Discourse Annotation'), ('discourseAnnotation-audienceReactions', 'Discourse Annotation - Audience Reactions'), ('discourseAnnotation-coreference', 'Discourse Annotation - Coreference'), ('discourseAnnotation-dialogueActs', 'Discourse Annotation - Dialogue Acts'), ('discourseAnnotation-discourseRelations', 'Discourse Annotation - Discourse Relations'), ('lemmatization', 'Lemmatization'), ('morphosyntacticAnnotation-bPosTagging', 'Morphosyntactic Annotation - B Pos Tagging'), ('morphosyntacticAnnotation-posTagging', 'Morphosyntactic Annotation - Pos Tagging'), ('segmentation', 'Segmentation'), ('semanticAnnotation', 'Semantic Annotation'), ('semanticAnnotation-certaintyLevel', 'Semantic Annotation - Certainty Level'), ('semanticAnnotation-emotions', 'Semantic Annotation - Emotions'), ('semanticAnnotation-entityMentions', 'Semantic Annotation - Entity Mentions'), ('semanticAnnotation-events', 'Semantic Annotation - Events'), ('semanticAnnotation-namedEntities', 'Semantic Annotation - Named Entities'), ('semanticAnnotation-polarity', 'Semantic Annotation - Polarity'), ('semanticAnnotation-questionTopicalTarget', 'Semantic Annotation - Question Topical Target'), ('semanticAnnotation-semanticClasses', 'Semantic Annotation - Semantic Classes'), ('semanticAnnotation-semanticRelations', 'Semantic Annotation - Semantic Relations'), ('semanticAnnotation-semanticRoles', 'Semantic Annotation - Semantic Roles'), ('semanticAnnotation-speechActs', 'Semantic Annotation - Speech Acts'), ('semanticAnnotation-temporalExpressions', 'Semantic Annotation - Temporal Expressions'), ('semanticAnnotation-textualEntailment', 'Semantic Annotation - Textual Entailment'), ('semanticAnnotation-wordSenses', 'Semantic Annotation - Word Senses'), ('speechAnnotation', 'Speech Annotation'), ('speechAnnotation-orthographicTranscription', 'Speech Annotation - Orthographic Transcription'), ('speechAnnotation-paralanguageAnnotation', 'Speech Annotation - Paralanguage Annotation'), ('speechAnnotation-phoneticTranscription', 'Speech Annotation - Phonetic Transcription'), ('speechAnnotation-prosodicAnnotation', 'Speech Annotation - Prosodic Annotation'), ('speechAnnotation-soundEvents', 'Speech Annotation - Sound Events'), ('speechAnnotation-soundToTextAlignment', 'Speech Annotation - Sound To Text Alignment'), ('speechAnnotation-speakerIdentification', 'Speech Annotation - Speaker Identification'), ('speechAnnotation-speakerTurns', 'Speech Annotation - Speaker Turns'), ('speechAnnotation', 'Speech Annotation'), ('stemming', 'Stemming'), ('structuralAnnotation', 'Structural Annotation'), ('syntacticAnnotation-shallowParsing', 'Syntactic Annotation - Shallow Parsing'), ('syntacticAnnotation-subcategorizationFrames', 'Syntactic Annotation - Subcategorization Frames'), ('syntacticAnnotation-treebanks', 'Syntactic Annotation - Treebanks'), ('syntacticosemanticAnnotation-links', 'Syntacticosemantic Annotation - Links'), ('translation', 'Translation'), ('transliteration', 'Transliteration'), ('discourseAnnotation-dialogueActs', 'Discourse Annotation - Dialogue Acts'), ('modalityAnnotation-bodyMovements', 'Modality Annotation - Body Movements'), ('modalityAnnotation-facialExpressions', 'Modality Annotation - Facial Expressions'), ('modalityAnnotation-gazeEyeMovements', 'Modality Annotation - Gaze Eye Movements'), ('modalityAnnotation-handArmGestures', 'Modality Annotation - Hand Arm Gestures'), ('modalityAnnotation-handManipulationOfObjects', 'Modality Annotation - Hand Manipulation Of Objects'), ('modalityAnnotation-headMovements', 'Modality Annotation - Head Movements'), ('modalityAnnotation-lipMovements', 'Modality Annotation - Lip Movements'), ('semanticAnnotation-emotions', 'Semantic Annotation - Emotions'), ('other', 'Other')])),
                ('annotationFormat', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Specifies the format that is used in the annotation process since often the mime type will not be sufficient for machine processing', max_length=100, verbose_name=b'Annotation format', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('tagset', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A name or a url reference to the tagset used in the annotation of the resource or used by the tool/service', max_length=500, verbose_name=b'Tagset', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('segmentationLevel', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the segmentation unit in terms of which the resource has been segmented or the level of segmentation a tool/service requires/outputs', max_length=5, verbose_name=b'Segmentation level', choices=[('paragraph', 'Paragraph'), ('sentence', 'Sentence'), ('clause', 'Clause'), ('word', 'Word'), ('wordGroup', 'Word Group'), ('utterance', 'Utterance'), ('topic', 'Topic'), ('signal', 'Signal'), ('phoneme', 'Phoneme'), ('syllable', 'Syllable'), ('phrase', 'Phrase'), ('diphone', 'Diphone'), ('prosodicBoundaries', 'Prosodic Boundaries'), ('frame', 'Frame'), ('scene', 'Scene'), ('shot', 'Shot'), ('other', 'Other')])),
                ('conformanceToStandardsBestPractices', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the standards or the best practices to which the tagset used for the annotation conforms', max_length=12, verbose_name=b'Conformance to standards best practices', choices=[('BLM', 'BLM'), ('CES', 'CES'), ('EAGLES', 'EAGLES'), ('EML', 'EML'), ('EMMA', 'EMMA'), ('GMX', 'GMX'), ('GrAF', 'GrAF'), ('HamNoSys', 'Ham No Sys'), ('InkML', 'InkML'), ('ISO12620', 'ISO12620'), ('ISO16642', 'ISO16642'), ('ISO1987', 'ISO1987'), ('ISO26162', 'ISO26162'), ('ISO30042', 'ISO30042'), ('ISO704', 'ISO704'), ('LMF', 'LMF'), ('MAF', 'MAF'), ('MLIF', 'MLIF'), ('MULTEXT', 'MULTEXT'), ('MUMIN', 'MUMIN'), ('multimodalInteractionFramework', 'Multimodal Interaction Framework'), ('OAXAL', 'OAXAL'), ('OWL', 'OWL'), ('pennTreeBank', 'Penn Tree Bank'), ('pragueTreebank', 'Prague Treebank'), ('RDF', 'RDF'), ('SemAF', 'SemAF'), ('SemAF_DA', 'SemAF_DA'), ('SemAF_NE', 'SemAF_NE'), ('SemAF_SRL', 'SemAF_SRL'), ('SemAF_DS', 'SemAF_DS'), ('SKOS', 'SKOS'), ('SRX', 'SRX'), ('SynAF', 'SynAF'), ('TBX', 'TBX'), ('TMX', 'TMX'), ('TEI', 'TEI'), ('TEI_P3', 'TEI_P3'), ('TEI_P4', 'TEI_P4'), ('TEI_P5', 'TEI_P5'), ('TimeML', 'TimeML'), ('XCES', 'XCES'), ('XLIFF', 'XLIFF'), ('WordNet', 'Word Net'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Input',
            },
        ),
        migrations.CreateModel(
            name='InvisibleStringModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='languageDescriptionEncodingInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encodingLevel', metashare.repository.fields.MultiSelectField(help_text=b'Information on the linguistic levels covered by the resource (grammar or lexical/conceptual resource)', max_length=2, verbose_name=b'Encoding level', choices=[('phonetics', 'Phonetics'), ('phonology', 'Phonology'), ('semantics', 'Semantics'), ('morphology', 'Morphology'), ('syntax', 'Syntax'), ('pragmatics', 'Pragmatics'), ('other', 'Other')])),
                ('conformanceToStandardsBestPractices', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the standards or the best practices to which the tagset used for the annotation conforms', max_length=12, verbose_name=b'Conformance to standards best practices', choices=[('BLM', 'BLM'), ('CES', 'CES'), ('EAGLES', 'EAGLES'), ('EML', 'EML'), ('EMMA', 'EMMA'), ('GMX', 'GMX'), ('GrAF', 'GrAF'), ('HamNoSys', 'Ham No Sys'), ('InkML', 'InkML'), ('ISO12620', 'ISO12620'), ('ISO16642', 'ISO16642'), ('ISO1987', 'ISO1987'), ('ISO26162', 'ISO26162'), ('ISO30042', 'ISO30042'), ('ISO704', 'ISO704'), ('LMF', 'LMF'), ('MAF', 'MAF'), ('MLIF', 'MLIF'), ('MULTEXT', 'MULTEXT'), ('MUMIN', 'MUMIN'), ('multimodalInteractionFramework', 'Multimodal Interaction Framework'), ('OAXAL', 'OAXAL'), ('OWL', 'OWL'), ('pennTreeBank', 'Penn Tree Bank'), ('pragueTreebank', 'Prague Treebank'), ('RDF', 'RDF'), ('SemAF', 'SemAF'), ('SemAF_DA', 'SemAF_DA'), ('SemAF_NE', 'SemAF_NE'), ('SemAF_SRL', 'SemAF_SRL'), ('SemAF_DS', 'SemAF_DS'), ('SKOS', 'SKOS'), ('SRX', 'SRX'), ('SynAF', 'SynAF'), ('TBX', 'TBX'), ('TMX', 'TMX'), ('TEI', 'TEI'), ('TEI_P3', 'TEI_P3'), ('TEI_P4', 'TEI_P4'), ('TEI_P5', 'TEI_P5'), ('TimeML', 'TimeML'), ('XCES', 'XCES'), ('XLIFF', 'XLIFF'), ('WordNet', 'Word Net'), ('other', 'Other')])),
                ('theoreticModel', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Name of the theoretic model applied for the creation/enrichment of the resource, and/or reference (URL or bibliographic reference) to informative material about the theoretic model used', max_length=500, verbose_name=b'Theoretic model', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('formalism', metashare.repository.fields.XmlCharField(help_text=b'Reference (name, bibliographic reference or link to url) for the formalism used for the creation/enrichment of the resource (grammar or tool/service)', max_length=1000, verbose_name=b'Formalism', blank=True)),
                ('task', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'An indication of the task performed by the grammar', max_length=3, verbose_name=b'Task', choices=[('anaphoraResolution', 'Anaphora Resolution'), ('chunking', 'Chunking'), ('parsing', 'Parsing'), ('npRecognition', 'Np Recognition'), ('titlesParsing', 'Titles Parsing'), ('definitionsParsing', 'Definitions Parsing'), ('analysis', 'Analysis'), ('generation', 'Generation'), ('other', 'Other')])),
                ('grammaticalPhenomenaCoverage', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'An indication of the grammatical phenomena covered by the grammar', max_length=2, verbose_name=b'Grammatical phenomena coverage', choices=[('clauseStructure', 'Clause Structure'), ('ppAttachment', 'Pp Attachment'), ('npStructure', 'Np Structure'), ('coordination', 'Coordination'), ('anaphora', 'Anaphora'), ('other', 'Other')])),
                ('weightedGrammar', metashare.repository.fields.MetaBooleanField(help_text=b'Indicates whether the grammar contains numerical weights (incl. probabilities)', verbose_name=b'Weighted grammar', choices=[(True, b'Yes'), (False, b'No')])),
            ],
            options={
                'verbose_name': 'Language description encoding',
            },
        ),
        migrations.CreateModel(
            name='languageDescriptionImageInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'image', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('creationInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation')),
                ('imageContentInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.imageContentInfoType_model', blank=True, help_text=b'Groups together information on the contents of the image part of a resource', verbose_name=b'Image content')),
            ],
            options={
                'verbose_name': 'Language description image',
            },
        ),
        migrations.CreateModel(
            name='languageDescriptionMediaTypeType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('languageDescriptionImageInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.languageDescriptionImageInfoType_model', blank=True, help_text=b'Groups together all information relevant to the image module of a language description (e.g. format, languages, size etc.), if there are any (e.g. for sign language grammars)', verbose_name=b'Language description image')),
            ],
            options={
                'verbose_name': 'Language description media',
            },
        ),
        migrations.CreateModel(
            name='languageDescriptionOperationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Language description operation',
            },
        ),
        migrations.CreateModel(
            name='languageDescriptionPerformanceInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('robustness', metashare.repository.fields.XmlCharField(help_text=b'Free text statement on the robustness of the grammar (how well the grammar can cope with misspelt/unknown etc. input, i.e. whether it can produce even partial interpretations of the input)', max_length=500, verbose_name=b'Robustness', blank=True)),
                ('shallowness', metashare.repository.fields.XmlCharField(help_text=b'Free text statement on the shallowness of the grammar (how deep the syntactic analysis performed by the grammar can be)', max_length=200, verbose_name=b'Shallowness', blank=True)),
                ('output', metashare.repository.fields.XmlCharField(help_text=b'Indicates whether the output of the operation of the grammar is a statement of grammaticality (grammatical/ungrammatical) or structures (interpretation of the input)', max_length=500, verbose_name=b'Output', blank=True)),
            ],
            options={
                'verbose_name': 'Language description performance',
            },
        ),
        migrations.CreateModel(
            name='languageDescriptionTextInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'text', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('creationInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation')),
            ],
            options={
                'verbose_name': 'Language description text',
            },
        ),
        migrations.CreateModel(
            name='languageDescriptionVideoInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'video', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('creationInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation')),
            ],
            options={
                'verbose_name': 'Language description video',
            },
        ),
        migrations.CreateModel(
            name='languageInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('languageId', metashare.repository.fields.XmlCharField(help_text=b'The identifier of the language that is included in the resource or supported by the tool/service; an autocompletion mechanism with values from the ISO 639 is provided in the editor, but the values can be subsequently edited for further specification (according to the IETF BCP47 guidelines)', max_length=100, verbose_name=b'Language id')),
                ('languageName', metashare.repository.fields.XmlCharField(help_text=b'A human understandable name of the language that is used in the resource or supported by the tool/service; an autocompletion mechanism with values from the ISO 639 is provided in the editor, but the values can be subsequently edited for further specification (according to the IETF BCP47 guidelines)', max_length=100, verbose_name=b'Language name')),
                ('languageScript', metashare.repository.fields.XmlCharField(help_text=b'Specifies the writing system used to represent the language in form of a four letter code as it is defined in ISO-15924', max_length=100, verbose_name=b'Language script', blank=True)),
                ('back_to_corpusaudioinfotype_model', models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True)),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextngraminfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True)),
                ('back_to_corpusvideoinfotype_model', models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True)),
                ('back_to_languagedescriptionimageinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionImageInfoType_model', null=True)),
                ('back_to_languagedescriptiontextinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionTextInfoType_model', null=True)),
                ('back_to_languagedescriptionvideoinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionVideoInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Language',
            },
        ),
        migrations.CreateModel(
            name='languageVarietyInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('languageVarietyType', models.CharField(help_text=b'Specifies the type of the language variety that occurs in the resource or is supported by a tool/service', max_length=20, verbose_name=b'Language variety type', choices=[('dialect', 'Dialect'), ('jargon', 'Jargon'), ('other', 'Other')])),
                ('languageVarietyName', metashare.repository.fields.XmlCharField(help_text=b'The name of the language variety that occurs in the resource or is supported by a tool/service', max_length=100, verbose_name=b'Language variety name')),
            ],
            options={
                'verbose_name': 'Language variety',
            },
        ),
        migrations.CreateModel(
            name='lexicalConceptualResourceAudioInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'audio', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('audioContentInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.audioContentInfoType_model', blank=True, help_text=b'Groups together information on the contents of the audio part of a resource', verbose_name=b'Audio content')),
            ],
            options={
                'verbose_name': 'Lexical conceptual resource audio',
            },
        ),
        migrations.CreateModel(
            name='lexicalConceptualResourceEncodingInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encodingLevel', metashare.repository.fields.MultiSelectField(help_text=b'Information on the contents of the lexicalConceptualResource as regards the linguistic level of analysis', max_length=2, verbose_name=b'Encoding level', choices=[('phonetics', 'Phonetics'), ('phonology', 'Phonology'), ('semantics', 'Semantics'), ('morphology', 'Morphology'), ('syntax', 'Syntax'), ('pragmatics', 'Pragmatics'), ('other', 'Other')])),
                ('linguisticInformation', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'A more detailed account of the linguistic information contained in the lexicalConceptualResource', max_length=13, verbose_name=b'Linguistic information', choices=[('accentuation', 'Accentuation'), ('lemma', 'Lemma'), ('lemma-MultiWordUnits', 'Lemma - Multi Word Units'), ('lemma-Variants', 'Lemma - Variants'), ('lemma-Abbreviations', 'Lemma - Abbreviations'), ('lemma-Compounds', 'Lemma - Compounds'), ('lemma-CliticForms', 'Lemma - Clitic Forms'), ('partOfSpeech', 'Part Of Speech'), ('morpho-Case', 'Morpho - Case'), ('morpho-Gender', 'Morpho - Gender'), ('morpho-Number', 'Morpho - Number'), ('morpho-Degree', 'Morpho - Degree'), ('morpho-IrregularForms', 'Morpho - Irregular Forms'), ('morpho-Mood', 'Morpho - Mood'), ('morpho-Tense', 'Morpho - Tense'), ('morpho-Person', 'Morpho - Person'), ('morpho-Aspect', 'Morpho - Aspect'), ('morpho-Voice', 'Morpho - Voice'), ('morpho-Auxiliary', 'Morpho - Auxiliary'), ('morpho-Inflection', 'Morpho - Inflection'), ('morpho-Reflexivity', 'Morpho - Reflexivity'), ('syntax-SubcatFrame', 'Syntax - Subcat Frame'), ('semantics-Traits', 'Semantics - Traits'), ('semantics-SemanticClass', 'Semantics - Semantic Class'), ('semantics-CrossReferences', 'Semantics - Cross References'), ('semantics-Relations', 'Semantics - Relations'), ('semantics-Relations-Hyponyms', 'Semantics - Relations - Hyponyms'), ('semantics-Relations-Hyperonyms', 'Semantics - Relations - Hyperonyms'), ('semantics-Relations-Synonyms', 'Semantics - Relations - Synonyms'), ('semantics-Relations-Antonyms', 'Semantics - Relations - Antonyms'), ('semantics-Relations-Troponyms', 'Semantics - Relations - Troponyms'), ('semantics-Relations-Meronyms', 'Semantics - Relations - Meronyms'), ('usage-Frequency', 'Usage - Frequency'), ('usage-Register', 'Usage - Register'), ('usage-Collocations', 'Usage - Collocations'), ('usage-Examples', 'Usage - Examples'), ('usage-Notes', 'Usage - Notes'), ('definition/gloss', 'Definition/gloss'), ('translationEquivalent', 'Translation Equivalent'), ('phonetics-Transcription', 'Phonetics - Transcription'), ('semantics-Domain', 'Semantics - Domain'), ('semantics-EventType', 'Semantics - Event Type'), ('semantics-SemanticRoles', 'Semantics - Semantic Roles'), ('statisticalProperties', 'Statistical Properties'), ('morpho-Derivation', 'Morpho - Derivation'), ('semantics-QualiaStructure', 'Semantics - Qualia Structure'), ('syntacticoSemanticLinks', 'Syntactico Semantic Links'), ('other', 'Other')])),
                ('conformanceToStandardsBestPractices', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the standards or the best practices to which the tagset used for the annotation conforms', max_length=12, verbose_name=b'Conformance to standards best practices', choices=[('BLM', 'BLM'), ('CES', 'CES'), ('EAGLES', 'EAGLES'), ('EML', 'EML'), ('EMMA', 'EMMA'), ('GMX', 'GMX'), ('GrAF', 'GrAF'), ('HamNoSys', 'Ham No Sys'), ('InkML', 'InkML'), ('ISO12620', 'ISO12620'), ('ISO16642', 'ISO16642'), ('ISO1987', 'ISO1987'), ('ISO26162', 'ISO26162'), ('ISO30042', 'ISO30042'), ('ISO704', 'ISO704'), ('LMF', 'LMF'), ('MAF', 'MAF'), ('MLIF', 'MLIF'), ('MULTEXT', 'MULTEXT'), ('MUMIN', 'MUMIN'), ('multimodalInteractionFramework', 'Multimodal Interaction Framework'), ('OAXAL', 'OAXAL'), ('OWL', 'OWL'), ('pennTreeBank', 'Penn Tree Bank'), ('pragueTreebank', 'Prague Treebank'), ('RDF', 'RDF'), ('SemAF', 'SemAF'), ('SemAF_DA', 'SemAF_DA'), ('SemAF_NE', 'SemAF_NE'), ('SemAF_SRL', 'SemAF_SRL'), ('SemAF_DS', 'SemAF_DS'), ('SKOS', 'SKOS'), ('SRX', 'SRX'), ('SynAF', 'SynAF'), ('TBX', 'TBX'), ('TMX', 'TMX'), ('TEI', 'TEI'), ('TEI_P3', 'TEI_P3'), ('TEI_P4', 'TEI_P4'), ('TEI_P5', 'TEI_P5'), ('TimeML', 'TimeML'), ('XCES', 'XCES'), ('XLIFF', 'XLIFF'), ('WordNet', 'Word Net'), ('other', 'Other')])),
                ('theoreticModel', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Name of the theoretic model applied for the creation/enrichment of the resource, and/or reference (URL or bibliographic reference) to informative material about the theoretic model used', max_length=500, verbose_name=b'Theoretic model', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('externalRef', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Another resource to which the lexicalConceptualResource is linked (e.g. link to a wordnet or ontology)', max_length=100, verbose_name=b'External ref', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('extratextualInformation', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'An indication of the extratextual information contained in the lexicalConceptualResouce; can be used as an alternative to audio, image, videos etc. for cases where these are not considered an important part of the lcr', max_length=2, verbose_name=b'Extratextual information', choices=[('images', 'Images'), ('videos', 'Videos'), ('soundRecordings', 'Sound Recordings'), ('other', 'Other')])),
                ('extraTextualInformationUnit', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The unit of the extratextual information contained in the lexical conceptual resource', max_length=2, verbose_name=b'Extratextual information unit', choices=[('word', 'Word'), ('lemma', 'Lemma'), ('semantics', 'Semantics'), ('example', 'Example'), ('syntax', 'Syntax'), ('lexicalUnit', 'Lexical Unit'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Lexical conceptual resource encoding',
            },
        ),
        migrations.CreateModel(
            name='lexicalConceptualResourceImageInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'image', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
                ('imageContentInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.imageContentInfoType_model', blank=True, help_text=b'Groups together information on the contents of the image part of a resource', verbose_name=b'Image content')),
            ],
            options={
                'verbose_name': 'Lexical conceptual resource image',
            },
        ),
        migrations.CreateModel(
            name='lexicalConceptualResourceMediaTypeType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lexicalConceptualResourceAudioInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lexicalConceptualResourceAudioInfoType_model', blank=True, help_text=b'Groups information on the audio part of the lexical/conceptual resource', verbose_name=b'Lexical conceptual resource audio')),
                ('lexicalConceptualResourceImageInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lexicalConceptualResourceImageInfoType_model', blank=True, help_text=b'Groups information on the image part of the lexical/conceptual resource', verbose_name=b'Lexical conceptual resource image')),
            ],
            options={
                'verbose_name': 'Lexical conceptual resource media',
            },
        ),
        migrations.CreateModel(
            name='lexicalConceptualResourceTextInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'text', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
            ],
            options={
                'verbose_name': 'Lexical conceptual resource text',
            },
        ),
        migrations.CreateModel(
            name='lexicalConceptualResourceVideoInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.XmlCharField(default=b'video', help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=1000, editable=False, verbose_name=b'Media')),
            ],
            options={
                'verbose_name': 'Lexical conceptual resource video',
            },
        ),
        migrations.CreateModel(
            name='licenceInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('licence', metashare.repository.fields.MultiSelectField(help_text=b'The licence of use for the resource; for an overview of licences, please visit: http://www.meta-net.eu/meta-share/licenses', max_length=11, verbose_name=b'Licence', choices=[('CC-BY', 'CC - BY'), ('CC-BY-NC', 'CC - BY - NC'), ('CC-BY-NC-ND', 'CC - BY - NC - ND'), ('CC-BY-NC-SA', 'CC - BY - NC - SA'), ('CC-BY-ND', 'CC - BY - ND'), ('CC-BY-SA', 'CC - BY - SA'), ('CC-ZERO', 'CC - ZERO'), ('MS-C-NoReD', 'MS - C - No ReD'), ('MS-C-NoReD-FF', 'MS - C - No ReD - FF'), ('MS-C-NoReD-ND', 'MS - C - No ReD - ND'), ('MS-C-NoReD-ND-FF', 'MS - C - No ReD - ND - FF'), ('MS-NC-NoReD', 'MS - NC - No ReD'), ('MS-NC-NoReD-FF', 'MS - NC - No ReD - FF'), ('MS-NC-NoReD-ND', 'MS - NC - No ReD - ND'), ('MS-NC-NoReD-ND-FF', 'MS - NC - No ReD - ND - FF'), ('MSCommons-BY', 'MS Commons - BY'), ('MSCommons-BY-NC', 'MS Commons - BY - NC'), ('MSCommons-BY-NC-ND', 'MS Commons - BY - NC - ND'), ('MSCommons-BY-NC-SA', 'MS Commons - BY - NC - SA'), ('MSCommons-BY-ND', 'MS Commons - BY - ND'), ('MSCommons-BY-SA', 'MS Commons - BY - SA'), ('CLARIN_ACA', 'CLARIN_ACA'), ('CLARIN_ACA-NC', 'CLARIN_ACA - NC'), ('CLARIN_PUB', 'CLARIN_PUB'), ('CLARIN_RES', 'CLARIN_RES'), ('ELRA_END_USER', 'ELRA_END_USER'), ('ELRA_EVALUATION', 'ELRA_EVALUATION'), ('ELRA_VAR', 'ELRA_VAR'), ('ELRA_VAR_E', 'ELRA_VAR_E'), ('AGPL', 'AGPL'), ('ApacheLicence_2.0', 'Apache Licence_2.0'), ('BSD', 'BSD'), ('BSD-style', 'BSD - Style'), ('GFDL', 'GFDL'), ('GPL', 'GPL'), ('LGPL', 'LGPL'), ('Princeton_Wordnet', 'Princeton_ Wordnet'), ('proprietary', 'Proprietary'), ('underNegotiation', 'Under Negotiation'), ('other', 'Other')])),
                ('restrictionsOfUse', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the restrictions imposed by the licence', max_length=3, verbose_name=b'Restrictions of use', choices=[('informLicensor', 'Inform Licensor'), ('redeposit', 'Redeposit'), ('onlyMSmembers', 'OnlyM Smembers'), ('academic-nonCommercialUse', 'Academic - Non Commercial Use'), ('evaluationUse', 'Evaluation Use'), ('commercialUse', 'Commercial Use'), ('attribution', 'Attribution'), ('shareAlike', 'Share Alike'), ('noDerivatives', 'No Derivatives'), ('noRedistribution', 'No Redistribution'), ('other', 'Other')])),
                ('distributionAccessMedium', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the medium (channel) used for delivery or providing access to the resource', max_length=3, verbose_name=b'Distribution access medium', choices=[('webExecutable', 'Web Executable'), ('paperCopy', 'Paper Copy'), ('hardDisk', 'Hard Disk'), ('bluRay', 'Blu Ray'), ('DVD-R', 'DVD - R'), ('CD-ROM', 'CD - ROM'), ('downloadable', 'Downloadable'), ('accessibleThroughInterface', 'Accessible Through Interface'), ('other', 'Other')])),
                ('downloadLocation', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Any url where the resource can be downloaded from', max_length=1000, verbose_name=b'Download location', validators=[django.core.validators.RegexValidator(b"^(?i)((http|ftp)s?):\\/\\/(([a-z0-9.-]|%[0-9A-F]{2}){3,})(:(\\d+))?((\\/([a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(\\?(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(#(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(?!\\r?\\n)$", b'Not a valid URL value (must not contain non-ASCII characters, for example; see also RFC 2396).', django.core.exceptions.ValidationError)])),
                ('executionLocation', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Any url where the service providing access to a resource is being executed', max_length=1000, verbose_name=b'Execution location', validators=[django.core.validators.RegexValidator(b"^(?i)((http|ftp)s?):\\/\\/(([a-z0-9.-]|%[0-9A-F]{2}){3,})(:(\\d+))?((\\/([a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(\\?(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(#(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(?!\\r?\\n)$", b'Not a valid URL value (must not contain non-ASCII characters, for example; see also RFC 2396).', django.core.exceptions.ValidationError)])),
                ('fee', metashare.repository.fields.XmlCharField(help_text=b'Specifies the costs that are required to access the resource, a fragment of the resource or to use a tool or service', max_length=100, verbose_name=b'Fee', blank=True)),
                ('attributionText', metashare.repository.fields.DictField(blank=True, help_text=b'The text that must be quoted for attribution purposes when using a resource - for cases where a resource is provided with a restriction on attribution', null=True, verbose_name=b'Attribution text', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('userNature', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The conditions imposed by the nature of the user (for instance, a research use may have different implications depending on this)', max_length=1, verbose_name=b'User nature', choices=[('academic', 'Academic'), ('commercial', 'Commercial')])),
                ('back_to_distributioninfotype_model', models.ForeignKey(blank=True, to='repository.distributionInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Licence',
            },
        ),
        migrations.CreateModel(
            name='lingualityInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lingualityType', models.CharField(help_text=b'Indicates whether the resource includes one, two or more languages', max_length=20, verbose_name=b'Linguality type', choices=[('bilingual', 'Bilingual'), ('monolingual', 'Monolingual'), ('multilingual', 'Multilingual')])),
                ('multilingualityType', models.CharField(blank=True, help_text=b'Indicates whether the corpus is parallel, comparable or mixed', max_length=30, verbose_name=b'Multilinguality type', choices=[('comparable', 'Comparable'), ('multilingualSingleText', 'Multilingual Single Text'), ('other', 'Other'), ('parallel', 'Parallel')])),
                ('multilingualityTypeDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on multilinguality of a resource in free text', max_length=512, verbose_name=b'Multilinguality type details', blank=True)),
            ],
            options={
                'verbose_name': 'Linguality',
            },
        ),
        migrations.CreateModel(
            name='linkToOtherMediaInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('otherMedia', models.CharField(help_text=b'Specifies the media types that are linked to the media type described within the same resource', max_length=30, verbose_name=b'Other media', choices=[('audio', 'Audio'), ('image', 'Image'), ('text', 'Text'), ('textNumerical', 'Text Numerical'), ('video', 'Video')])),
                ('mediaTypeDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on the way the media types are linked and/or synchronized with each other within the same resource', max_length=500, verbose_name=b'Media details', blank=True)),
                ('synchronizedWithText', metashare.repository.fields.MetaBooleanField(help_text=b'Whether video, text and textNumerical media type is synchronized with text within the same resource', verbose_name=b'Synchronized with text', choices=[(True, b'Yes'), (False, b'No')])),
                ('synchronizedWithAudio', metashare.repository.fields.MetaBooleanField(help_text=b'Whether text, video or textNumerical media type is synchronized with audio within the same resource', verbose_name=b'Synchronized with audio', choices=[(True, b'Yes'), (False, b'No')])),
                ('synchronizedWithVideo', metashare.repository.fields.MetaBooleanField(help_text=b'Whether text or textNumerical media type is synchronized with video within the same resource', verbose_name=b'Synchronized with video', choices=[(True, b'Yes'), (False, b'No')])),
                ('sycnhronizedWithImage', metashare.repository.fields.MetaBooleanField(help_text=b'Whether text or textNumerical media type is synchronized with image within the same resource', verbose_name=b'Sycnhronized with image', choices=[(True, b'Yes'), (False, b'No')])),
                ('synchronizedWithTextNumerical', metashare.repository.fields.MetaBooleanField(help_text=b'Whether video or audio media type is synchronized with the textNumerical (representation of sensorimotor measurements) within the same resource', verbose_name=b'Synchronized with text numerical', choices=[(True, b'Yes'), (False, b'No')])),
                ('back_to_corpusaudioinfotype_model', models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True)),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextnumericalinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNumericalInfoType_model', null=True)),
                ('back_to_corpusvideoinfotype_model', models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True)),
                ('back_to_languagedescriptionimageinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionImageInfoType_model', null=True)),
                ('back_to_languagedescriptiontextinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionTextInfoType_model', null=True)),
                ('back_to_languagedescriptionvideoinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionVideoInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Link to other media',
            },
        ),
        migrations.CreateModel(
            name='membershipInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member', metashare.repository.fields.MetaBooleanField(help_text=b'Whether the user is a member or not', verbose_name=b'Member', choices=[(True, b'Yes'), (False, b'No')])),
                ('membershipInstitution', metashare.repository.fields.MultiSelectField(help_text=b'This lists the different institutions releasing the resources and establishing membership conditions', max_length=2, verbose_name=b'Membership institution', choices=[('ELRA', 'ELRA'), ('LDC', 'LDC'), ('TST-CENTRALE', 'TST - CENTRALE'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Membership',
            },
        ),
        migrations.CreateModel(
            name='metadataInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metadataCreationDate', models.DateField(help_text=b'The date of creation of this metadata description (automatically inserted by the MetaShare software)', verbose_name=b'Metadata creation date')),
                ('source', metashare.repository.fields.XmlCharField(help_text=b'Refers to the catalogue or repository from which the metadata has been originated', max_length=500, verbose_name=b'Source', blank=True)),
                ('originalMetadataSchema', metashare.repository.fields.XmlCharField(help_text=b'Refers to the metadata schema originally used for the description of the resource', max_length=500, verbose_name=b'Original metadata schema', blank=True)),
                ('originalMetadataLink', metashare.repository.fields.XmlCharField(blank=True, help_text=b'A link to the original metadata record, in cases of harvesting', max_length=1000, verbose_name=b'Original metadata link', validators=[django.core.validators.RegexValidator(b"^(?i)((http|ftp)s?):\\/\\/(([a-z0-9.-]|%[0-9A-F]{2}){3,})(:(\\d+))?((\\/([a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(\\?(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(#(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(?!\\r?\\n)$", b'Not a valid URL value (must not contain non-ASCII characters, for example; see also RFC 2396).', django.core.exceptions.ValidationError)])),
                ('metadataLanguageName', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The name of the language in which the metadata description is written; an autocompletion mechanism with values from the ISO 639 is provided in the editor, but the values can be subsequently edited for further specification (according to the IETF BCP47 guidelines)', max_length=1000, verbose_name=b'Metadata language name', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('metadataLanguageId', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The identifier of the language in which the metadata description is written; an autocompletion mechanism with values from the ISO 639 is provided in the editor, but the values can be subsequently edited for further specification (according to the IETF BCP47 guidelines)', max_length=1000, verbose_name=b'Metadata language id', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('metadataLastDateUpdated', models.DateField(help_text=b'The date of the last updating of the metadata record (automatically inserted by the MetaShare software)', null=True, verbose_name=b'Metadata last date updated', blank=True)),
                ('revision', metashare.repository.fields.XmlCharField(help_text=b'Provides an account of the revisions in free text or a link to a document with revisions', max_length=500, verbose_name=b'Revision', blank=True)),
            ],
            options={
                'verbose_name': 'Metadata',
            },
        ),
        migrations.CreateModel(
            name='modalityInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modalityType', metashare.repository.fields.MultiSelectField(help_text=b'Specifies the type of the modality represented in the resource or processed by a tool/service', max_length=3, verbose_name=b'Modality type', choices=[('bodyGesture', 'Body Gesture'), ('facialExpression', 'Facial Expression'), ('voice', 'Voice'), ('combinationOfModalities', 'Combination Of Modalities'), ('signLanguage', 'Sign Language'), ('spokenLanguage', 'Spoken Language'), ('writtenLanguage', 'Written Language'), ('other', 'Other')])),
                ('modalityTypeDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on modalities', max_length=500, verbose_name=b'Modality type details', blank=True)),
                ('back_to_corpusaudioinfotype_model', models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True)),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextnumericalinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNumericalInfoType_model', null=True)),
                ('back_to_languagedescriptionimageinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionImageInfoType_model', null=True)),
                ('back_to_languagedescriptionvideoinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionVideoInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourceaudioinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceAudioInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourceimageinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceImageInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourcetextinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceTextInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourcevideoinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceVideoInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Modality',
                'verbose_name_plural': 'Modalities',
            },
        ),
        migrations.CreateModel(
            name='ngramInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('baseItem', metashare.repository.fields.MultiSelectField(help_text=b'Type of item that is represented in the n-gram resource', max_length=2, verbose_name=b'Base item', choices=[('word', 'Word'), ('syllable', 'Syllable'), ('letter', 'Letter'), ('phoneme', 'Phoneme'), ('other', 'Other')])),
                ('order', models.IntegerField(help_text=b'The maximum number of items in the sequence', verbose_name=b'Order')),
                ('perplexity', models.FloatField(help_text=b'Derived from running on test set taken from the same corpus', null=True, verbose_name=b'Perplexity', blank=True)),
                ('isFactored', metashare.repository.fields.MetaBooleanField(help_text=b'Specifies whether the model is factored or not', verbose_name=b'Is factored', choices=[(True, b'Yes'), (False, b'No')])),
                ('factors', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The list of factors that have been used for the n-gram model', max_length=150, verbose_name=b'Factors', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('smoothing', metashare.repository.fields.XmlCharField(help_text=b'The technique used for giving unseen items some probability', max_length=1000, verbose_name=b'Smoothing', blank=True)),
                ('interpolated', metashare.repository.fields.MetaBooleanField(help_text=b'Interpolated language models are constructed by 2 or more corpora. Each corpus is represented in the model according to a predefined weight.', verbose_name=b'Interpolated', choices=[(True, b'Yes'), (False, b'No')])),
            ],
            options={
                'verbose_name': 'Ngram',
            },
        ),
        migrations.CreateModel(
            name='organizationListType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Organization list',
            },
        ),
        migrations.CreateModel(
            name='outputInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mediaType', metashare.repository.fields.MultiSelectField(help_text=b'Specifies the media type of the resource and basically corresponds to the physical medium of the content representation. Each media type is described through a distinctive set of features. A resource may consist of parts attributed to different types of media. A tool/service may take as input/output more than one different media types.', max_length=2, verbose_name=b'Media type', choices=[('text', 'Text'), ('audio', 'Audio'), ('video', 'Video'), ('image', 'Image'), ('textNumerical', 'Text Numerical')])),
                ('resourceType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The type of the resource that a tool or service takes as input or produces as output', max_length=1, verbose_name=b'Resource type', choices=[('corpus', 'Corpus'), ('lexicalConceptualResource', 'Lexical Conceptual Resource'), ('languageDescription', 'Language Description')])),
                ('modalityType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the type of the modality represented in the resource or processed by a tool/service', max_length=3, verbose_name=b'Modality type', choices=[('bodyGesture', 'Body Gesture'), ('facialExpression', 'Facial Expression'), ('voice', 'Voice'), ('combinationOfModalities', 'Combination Of Modalities'), ('signLanguage', 'Sign Language'), ('spokenLanguage', 'Spoken Language'), ('writtenLanguage', 'Written Language'), ('other', 'Other')])),
                ('languageName', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A human understandable name of the language that is used in the resource or supported by the tool/service according to the IETF BCP47 standard', max_length=100, verbose_name=b'Language name', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('languageId', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The identifier of the language that is included in the resource or supported by the tool/service according to the IETF BCP47 standard', max_length=100, verbose_name=b'Language id', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('languageVarietyName', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Specifies the type of the language variety that occurs in the resource or is supported by a tool/service', max_length=100, verbose_name=b'Language variety name', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('mimeType', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The mime-type of the resource which is a formalized specifier for the format included or a mime-type that the tool/service accepts; value to be taken from a subset of the official mime types of the Internet Assigned Numbers Authority (http://www.iana.org/)', max_length=50, verbose_name=b'Mime type', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('characterEncoding', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The name of the character encoding used in the resource or accepted by the tool/service', max_length=36, verbose_name=b'Character encoding', choices=[('US-ASCII', 'US - ASCII'), ('windows-1250', 'Windows - 1250'), ('windows-1251', 'Windows - 1251'), ('windows-1252', 'Windows - 1252'), ('windows-1253', 'Windows - 1253'), ('windows-1254', 'Windows - 1254'), ('windows-1257', 'Windows - 1257'), ('ISO-8859-1', 'ISO - 8859 - 1'), ('ISO-8859-2', 'ISO - 8859 - 2'), ('ISO-8859-4', 'ISO - 8859 - 4'), ('ISO-8859-5', 'ISO - 8859 - 5'), ('ISO-8859-7', 'ISO - 8859 - 7'), ('ISO-8859-9', 'ISO - 8859 - 9'), ('ISO-8859-13', 'ISO - 8859 - 13'), ('ISO-8859-15', 'ISO - 8859 - 15'), ('KOI8-R', 'KOI8 - R'), ('UTF-8', 'UTF - 8'), ('UTF-16', 'UTF - 16'), ('UTF-16BE', 'UTF - 16BE'), ('UTF-16LE', 'UTF - 16LE'), ('windows-1255', 'Windows - 1255'), ('windows-1256', 'Windows - 1256'), ('windows-1258', 'Windows - 1258'), ('ISO-8859-3', 'ISO - 8859 - 3'), ('ISO-8859-6', 'ISO - 8859 - 6'), ('ISO-8859-8', 'ISO - 8859 - 8'), ('windows-31j', 'Windows - 31j'), ('EUC-JP', 'EUC - JP'), ('x-EUC-JP-LINUX', 'X - EUC - JP - LINUX'), ('Shift_JIS', 'Shift_JIS'), ('ISO-2022-JP', 'ISO - 2022 - JP'), ('x-mswin-936', 'X - Mswin - 936'), ('GB18030', 'GB18030'), ('x-EUC-CN', 'X - EUC - CN'), ('GBK', 'GBK'), ('ISCII91', 'ISCII91'), ('x-windows-949', 'X - Windows - 949'), ('EUC-KR', 'EUC - KR'), ('ISO-2022-KR', 'ISO - 2022 - KR'), ('x-windows-950', 'X - Windows - 950'), ('x-MS950-HKSCS', 'X - MS950 - HKSCS'), ('x-EUC-TW', 'X - EUC - TW'), ('Big5', 'Big5'), ('Big5-HKSCS', 'Big5 - HKSCS'), ('TIS-620', 'TIS - 620'), ('Big5_Solaris', 'Big5_ Solaris'), ('Cp037', 'Cp037'), ('Cp273', 'Cp273'), ('Cp277', 'Cp277'), ('Cp278', 'Cp278'), ('Cp280', 'Cp280'), ('Cp284', 'Cp284'), ('Cp285', 'Cp285'), ('Cp297', 'Cp297'), ('Cp420', 'Cp420'), ('Cp424', 'Cp424'), ('Cp437', 'Cp437'), ('Cp500', 'Cp500'), ('Cp737', 'Cp737'), ('Cp775', 'Cp775'), ('Cp838', 'Cp838'), ('Cp850', 'Cp850'), ('Cp852', 'Cp852'), ('Cp855', 'Cp855'), ('Cp856', 'Cp856'), ('Cp857', 'Cp857'), ('Cp858', 'Cp858'), ('Cp860', 'Cp860'), ('Cp861', 'Cp861'), ('Cp862', 'Cp862'), ('Cp863', 'Cp863'), ('Cp864', 'Cp864'), ('Cp865', 'Cp865'), ('Cp866', 'Cp866'), ('Cp868', 'Cp868'), ('Cp869', 'Cp869'), ('Cp870', 'Cp870'), ('Cp871', 'Cp871'), ('Cp874', 'Cp874'), ('Cp875', 'Cp875'), ('Cp918', 'Cp918'), ('Cp921', 'Cp921'), ('Cp922', 'Cp922'), ('Cp930', 'Cp930'), ('Cp933', 'Cp933'), ('Cp935', 'Cp935'), ('Cp937', 'Cp937'), ('Cp939', 'Cp939'), ('Cp942', 'Cp942'), ('Cp942C', 'Cp942C'), ('Cp943', 'Cp943'), ('Cp943C', 'Cp943C'), ('Cp948', 'Cp948'), ('Cp949', 'Cp949'), ('Cp949C', 'Cp949C'), ('Cp950', 'Cp950'), ('Cp964', 'Cp964'), ('Cp970', 'Cp970'), ('Cp1006', 'Cp1006'), ('Cp1025', 'Cp1025'), ('Cp1026', 'Cp1026'), ('Cp1046', 'Cp1046'), ('Cp1047', 'Cp1047'), ('Cp1097', 'Cp1097'), ('Cp1098', 'Cp1098'), ('Cp1112', 'Cp1112'), ('Cp1122', 'Cp1122'), ('Cp1123', 'Cp1123'), ('Cp1124', 'Cp1124'), ('Cp1140', 'Cp1140'), ('Cp1141', 'Cp1141'), ('Cp1142', 'Cp1142'), ('Cp1143', 'Cp1143'), ('Cp1144', 'Cp1144'), ('Cp1145', 'Cp1145'), ('Cp1146', 'Cp1146'), ('Cp1147', 'Cp1147'), ('Cp1148', 'Cp1148'), ('Cp1149', 'Cp1149'), ('Cp1381', 'Cp1381'), ('Cp1383', 'Cp1383'), ('Cp33722', 'Cp33722'), ('ISO2022_CN_CNS', 'ISO2022_CN_CNS'), ('ISO2022_CN_GB', 'ISO2022_CN_GB'), ('JISAutoDetect', 'JIS Auto Detect'), ('MS874', 'MS874'), ('MacArabic', 'Mac Arabic'), ('MacCentralEurope', 'Mac Central Europe'), ('MacCroatian', 'Mac Croatian'), ('MacCyrillic', 'Mac Cyrillic'), ('MacDingbat', 'Mac Dingbat'), ('MacGreek', 'Mac Greek'), ('MacHebrew', 'Mac Hebrew'), ('MacIceland', 'Mac Iceland'), ('MacRoman', 'Mac Roman'), ('MacRomania', 'Mac Romania'), ('MacSymbol', 'Mac Symbol'), ('MacThai', 'Mac Thai'), ('MacTurkish', 'Mac Turkish'), ('MacUkraine', 'Mac Ukraine')])),
                ('annotationType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the annotation level of the resource or the annotation type a tool/ service requires or produces as an output', max_length=14, verbose_name=b'Annotation type', choices=[('alignment', 'Alignment'), ('discourseAnnotation', 'Discourse Annotation'), ('discourseAnnotation-audienceReactions', 'Discourse Annotation - Audience Reactions'), ('discourseAnnotation-coreference', 'Discourse Annotation - Coreference'), ('discourseAnnotation-dialogueActs', 'Discourse Annotation - Dialogue Acts'), ('discourseAnnotation-discourseRelations', 'Discourse Annotation - Discourse Relations'), ('lemmatization', 'Lemmatization'), ('morphosyntacticAnnotation-bPosTagging', 'Morphosyntactic Annotation - B Pos Tagging'), ('morphosyntacticAnnotation-posTagging', 'Morphosyntactic Annotation - Pos Tagging'), ('segmentation', 'Segmentation'), ('semanticAnnotation', 'Semantic Annotation'), ('semanticAnnotation-certaintyLevel', 'Semantic Annotation - Certainty Level'), ('semanticAnnotation-emotions', 'Semantic Annotation - Emotions'), ('semanticAnnotation-entityMentions', 'Semantic Annotation - Entity Mentions'), ('semanticAnnotation-events', 'Semantic Annotation - Events'), ('semanticAnnotation-namedEntities', 'Semantic Annotation - Named Entities'), ('semanticAnnotation-polarity', 'Semantic Annotation - Polarity'), ('semanticAnnotation-questionTopicalTarget', 'Semantic Annotation - Question Topical Target'), ('semanticAnnotation-semanticClasses', 'Semantic Annotation - Semantic Classes'), ('semanticAnnotation-semanticRelations', 'Semantic Annotation - Semantic Relations'), ('semanticAnnotation-semanticRoles', 'Semantic Annotation - Semantic Roles'), ('semanticAnnotation-speechActs', 'Semantic Annotation - Speech Acts'), ('semanticAnnotation-temporalExpressions', 'Semantic Annotation - Temporal Expressions'), ('semanticAnnotation-textualEntailment', 'Semantic Annotation - Textual Entailment'), ('semanticAnnotation-wordSenses', 'Semantic Annotation - Word Senses'), ('speechAnnotation', 'Speech Annotation'), ('speechAnnotation-orthographicTranscription', 'Speech Annotation - Orthographic Transcription'), ('speechAnnotation-paralanguageAnnotation', 'Speech Annotation - Paralanguage Annotation'), ('speechAnnotation-phoneticTranscription', 'Speech Annotation - Phonetic Transcription'), ('speechAnnotation-prosodicAnnotation', 'Speech Annotation - Prosodic Annotation'), ('speechAnnotation-soundEvents', 'Speech Annotation - Sound Events'), ('speechAnnotation-soundToTextAlignment', 'Speech Annotation - Sound To Text Alignment'), ('speechAnnotation-speakerIdentification', 'Speech Annotation - Speaker Identification'), ('speechAnnotation-speakerTurns', 'Speech Annotation - Speaker Turns'), ('speechAnnotation', 'Speech Annotation'), ('stemming', 'Stemming'), ('structuralAnnotation', 'Structural Annotation'), ('syntacticAnnotation-shallowParsing', 'Syntactic Annotation - Shallow Parsing'), ('syntacticAnnotation-subcategorizationFrames', 'Syntactic Annotation - Subcategorization Frames'), ('syntacticAnnotation-treebanks', 'Syntactic Annotation - Treebanks'), ('syntacticosemanticAnnotation-links', 'Syntacticosemantic Annotation - Links'), ('translation', 'Translation'), ('transliteration', 'Transliteration'), ('discourseAnnotation-dialogueActs', 'Discourse Annotation - Dialogue Acts'), ('modalityAnnotation-bodyMovements', 'Modality Annotation - Body Movements'), ('modalityAnnotation-facialExpressions', 'Modality Annotation - Facial Expressions'), ('modalityAnnotation-gazeEyeMovements', 'Modality Annotation - Gaze Eye Movements'), ('modalityAnnotation-handArmGestures', 'Modality Annotation - Hand Arm Gestures'), ('modalityAnnotation-handManipulationOfObjects', 'Modality Annotation - Hand Manipulation Of Objects'), ('modalityAnnotation-headMovements', 'Modality Annotation - Head Movements'), ('modalityAnnotation-lipMovements', 'Modality Annotation - Lip Movements'), ('semanticAnnotation-emotions', 'Semantic Annotation - Emotions'), ('other', 'Other')])),
                ('annotationFormat', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Specifies the format that is used in the annotation process since often the mime type will not be sufficient for machine processing', max_length=100, verbose_name=b'Annotation format', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('tagset', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A name or a url reference to the tagset used in the annotation of the resource or used by the tool/service', max_length=500, verbose_name=b'Tagset', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('segmentationLevel', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the segmentation unit in terms of which the resource has been segmented or the level of segmentation a tool/service requires/outputs', max_length=5, verbose_name=b'Segmentation level', choices=[('paragraph', 'Paragraph'), ('sentence', 'Sentence'), ('clause', 'Clause'), ('word', 'Word'), ('wordGroup', 'Word Group'), ('utterance', 'Utterance'), ('topic', 'Topic'), ('signal', 'Signal'), ('phoneme', 'Phoneme'), ('syllable', 'Syllable'), ('phrase', 'Phrase'), ('diphone', 'Diphone'), ('prosodicBoundaries', 'Prosodic Boundaries'), ('frame', 'Frame'), ('scene', 'Scene'), ('shot', 'Shot'), ('other', 'Other')])),
                ('conformanceToStandardsBestPractices', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the standards or the best practices to which the tagset used for the annotation conforms', max_length=12, verbose_name=b'Conformance to standards best practices', choices=[('BLM', 'BLM'), ('CES', 'CES'), ('EAGLES', 'EAGLES'), ('EML', 'EML'), ('EMMA', 'EMMA'), ('GMX', 'GMX'), ('GrAF', 'GrAF'), ('HamNoSys', 'Ham No Sys'), ('InkML', 'InkML'), ('ISO12620', 'ISO12620'), ('ISO16642', 'ISO16642'), ('ISO1987', 'ISO1987'), ('ISO26162', 'ISO26162'), ('ISO30042', 'ISO30042'), ('ISO704', 'ISO704'), ('LMF', 'LMF'), ('MAF', 'MAF'), ('MLIF', 'MLIF'), ('MULTEXT', 'MULTEXT'), ('MUMIN', 'MUMIN'), ('multimodalInteractionFramework', 'Multimodal Interaction Framework'), ('OAXAL', 'OAXAL'), ('OWL', 'OWL'), ('pennTreeBank', 'Penn Tree Bank'), ('pragueTreebank', 'Prague Treebank'), ('RDF', 'RDF'), ('SemAF', 'SemAF'), ('SemAF_DA', 'SemAF_DA'), ('SemAF_NE', 'SemAF_NE'), ('SemAF_SRL', 'SemAF_SRL'), ('SemAF_DS', 'SemAF_DS'), ('SKOS', 'SKOS'), ('SRX', 'SRX'), ('SynAF', 'SynAF'), ('TBX', 'TBX'), ('TMX', 'TMX'), ('TEI', 'TEI'), ('TEI_P3', 'TEI_P3'), ('TEI_P4', 'TEI_P4'), ('TEI_P5', 'TEI_P5'), ('TimeML', 'TimeML'), ('XCES', 'XCES'), ('XLIFF', 'XLIFF'), ('WordNet', 'Word Net'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Output',
            },
        ),
        migrations.CreateModel(
            name='participantInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', metashare.repository.fields.DictField(blank=True, help_text=b'The name of the person used instead of the real one', null=True, verbose_name=b'Alias', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('ageGroup', models.CharField(blank=True, help_text=b'The age group to which the participant belongs', max_length=30, verbose_name=b'Age group', choices=[('adult', 'Adult'), ('child', 'Child'), ('elderly', 'Elderly'), ('teenager', 'Teenager')])),
                ('age', metashare.repository.fields.XmlCharField(help_text=b'The age of the participant', max_length=50, verbose_name=b'Age', blank=True)),
                ('sex', models.CharField(blank=True, help_text=b'The gender of a person related to or participating in the resource', max_length=30, verbose_name=b'Sex', choices=[('female', 'Female'), ('male', 'Male'), ('unknown', 'Unknown')])),
                ('origin', models.CharField(blank=True, help_text=b'The language origin of the participant', max_length=30, verbose_name=b'Origin', choices=[('native', 'Native'), ('nonNative', 'Non Native'), ('unknown', 'Unknown')])),
                ('placeOfLiving', metashare.repository.fields.XmlCharField(help_text=b"The participant's place of living", max_length=100, verbose_name=b'Place of living', blank=True)),
                ('placeOfBirth', metashare.repository.fields.XmlCharField(help_text=b'The place in which the participant has been born', max_length=100, verbose_name=b'Place of birth', blank=True)),
                ('placeOfChildhood', metashare.repository.fields.XmlCharField(help_text=b'The place in which the participant lived as a child', max_length=100, verbose_name=b'Place of childhood', blank=True)),
                ('dialectAccent', metashare.repository.fields.DictField(blank=True, help_text=b'Provides information on the dialect of the participant', null=True, verbose_name=b'Dialect accent', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('speakingImpairment', metashare.repository.fields.XmlCharField(help_text=b'Provides information on any speaking impairment the participant may have', max_length=200, verbose_name=b'Speaking impairment', blank=True)),
                ('hearingImpairment', metashare.repository.fields.XmlCharField(help_text=b'Provides information on any hearing impairment the participant may have', max_length=200, verbose_name=b'Hearing impairment', blank=True)),
                ('smokingHabits', metashare.repository.fields.XmlCharField(help_text=b'Provides information on whether the participants smokes and on his/her smoking habits in general', max_length=100, verbose_name=b'Smoking habits', blank=True)),
                ('vocalTractConditions', models.CharField(blank=True, help_text=b'Provides information on the vocal tract conditions that may influence the speech of the participant', max_length=30, verbose_name=b'Vocal tract conditions', choices=[('dentalProsthesis', 'Dental Prosthesis'), ('other', 'Other')])),
                ('profession', metashare.repository.fields.XmlCharField(help_text=b"Provides information on the participant's profession", max_length=100, verbose_name=b'Profession', blank=True)),
                ('height', models.BigIntegerField(help_text=b'Provides information on the height of the participant in cm', null=True, verbose_name=b'Height', blank=True)),
                ('weight', models.BigIntegerField(help_text=b'Provides information on the weight of the participant', null=True, verbose_name=b'Weight', blank=True)),
                ('trainedSpeaker', metashare.repository.fields.MetaBooleanField(help_text=b'Provides information on whether the participant is trained in a specific task', verbose_name=b'Trained speaker', choices=[(True, b'Yes'), (False, b'No')])),
                ('placeOfSecondEducation', metashare.repository.fields.XmlCharField(help_text=b'Specifies the place of the secondary education of the participant', max_length=100, verbose_name=b'Place of second education', blank=True)),
                ('educationLevel', metashare.repository.fields.XmlCharField(help_text=b'Provides information on the education level of the participant', max_length=100, verbose_name=b'Education level', blank=True)),
            ],
            options={
                'verbose_name': 'Participant',
            },
        ),
        migrations.CreateModel(
            name='personListType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Person list',
            },
        ),
        migrations.CreateModel(
            name='personSourceSetInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numberOfPersons', models.BigIntegerField(help_text=b'The number of the persons participating in the audio or video part of the resource', null=True, verbose_name=b'Number of persons', blank=True)),
                ('ageOfPersons', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The age range of the group of participants; repeat the element if needed', max_length=2, verbose_name=b'Age of persons', choices=[('child', 'Child'), ('teenager', 'Teenager'), ('adult', 'Adult'), ('elderly', 'Elderly')])),
                ('ageRangeStart', models.BigIntegerField(help_text=b'Start of age range of the group of participants', null=True, verbose_name=b'Age range start', blank=True)),
                ('ageRangeEnd', models.BigIntegerField(help_text=b'End of age range of the group of participants', null=True, verbose_name=b'Age range end', blank=True)),
                ('sexOfPersons', models.CharField(blank=True, help_text=b'The gender of the group of participants', max_length=30, verbose_name=b'Sex of persons', choices=[('female', 'Female'), ('male', 'Male'), ('mixed', 'Mixed'), ('unknown', 'Unknown')])),
                ('originOfPersons', models.CharField(blank=True, help_text=b'The language origin of the group of participants', max_length=30, verbose_name=b'Origin of persons', choices=[('mixed', 'Mixed'), ('native', 'Native'), ('nonNative', 'Non Native'), ('unknown', 'Unknown')])),
                ('dialectAccentOfPersons', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Provides information on the dialect of the group of participants', max_length=500, verbose_name=b'Dialect accent of persons', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('geographicDistributionOfPersons', metashare.repository.fields.XmlCharField(help_text=b'Gives information on the geographic distribution of the participants', max_length=200, verbose_name=b'Geographic distribution of persons', blank=True)),
                ('hearingImpairmentOfPersons', models.CharField(blank=True, help_text=b'Whether the group of participants contains persons with hearing impairments', max_length=30, verbose_name=b'Hearing impairment of persons', choices=[('mixed', 'Mixed'), ('no', 'No'), ('yes', 'Yes')])),
                ('speakingImpairmentOfPersons', models.CharField(blank=True, help_text=b'Whether the group of participants contains persons withwith speakingimpairments', max_length=30, verbose_name=b'Speaking impairment of persons', choices=[('mixed', 'Mixed'), ('no', 'No'), ('yes', 'Yes')])),
                ('numberOfTrainedSpeakers', models.BigIntegerField(help_text=b'The number of participants that have been trained for the specific task', null=True, verbose_name=b'Number of trained speakers', blank=True)),
                ('speechInfluences', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the factors influencing speech', max_length=2, verbose_name=b'Speech influences', choices=[('alcohol', 'Alcohol'), ('sleepDeprivation', 'Sleep Deprivation'), ('hyperbaric', 'Hyperbaric'), ('medication', 'Medication'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Person source set',
            },
        ),
        migrations.CreateModel(
            name='projectInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectName', metashare.repository.fields.DictField(help_text=b'The full name of a project related to the resource', null=True, verbose_name=b'Project name', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('projectShortName', metashare.repository.fields.DictField(blank=True, help_text=b'A short name or abbreviation of a project related to the resource', null=True, verbose_name=b'Project short name', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('projectID', metashare.repository.fields.XmlCharField(help_text=b'An unambiguous referent to a project related to the resource', max_length=100, verbose_name=b'Project id', blank=True)),
                ('url', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A URL used as homepage of an entity (e.g. of a person, organization, resource etc.) and/or where an entity (e.g.LR, document etc.) is located', max_length=1000, verbose_name=b'Url', validators=[django.core.validators.RegexValidator(b"^(?i)((http|ftp)s?):\\/\\/(([a-z0-9.-]|%[0-9A-F]{2}){3,})(:(\\d+))?((\\/([a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(\\?(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(#(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(?!\\r?\\n)$", b'Not a valid URL value (must not contain non-ASCII characters, for example; see also RFC 2396).', django.core.exceptions.ValidationError)])),
                ('fundingType', metashare.repository.fields.MultiSelectField(help_text=b'Specifies the type of funding of the project', max_length=2, verbose_name=b'Funding type', choices=[('other', 'Other'), ('ownFunds', 'Own Funds'), ('nationalFunds', 'National Funds'), ('euFunds', 'Eu Funds')])),
                ('funder', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The full name of the funder of the project', max_length=100, verbose_name=b'Funder', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('fundingCountry', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The name of the funding country, in case of national funding as mentioned in ISO3166', max_length=100, verbose_name=b'Funding country', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('projectStartDate', models.DateField(help_text=b'The starting date of a project related to the resource', null=True, verbose_name=b'Project start date', blank=True)),
                ('projectEndDate', models.DateField(help_text=b'The end date of a project related to the resources', null=True, verbose_name=b'Project end date', blank=True)),
                ('source_url', models.URLField(default=b'http://127.0.0.1:8000', help_text=b'(Read-only) base URL for the server where the master copy of the associated entity instance is located.')),
                ('copy_status', models.CharField(default=b'm', help_text=b'Generalized copy status flag for this entity instance.', max_length=1, choices=[(b'm', b'master copy'), (b'r', b'remote copy'), (b'p', b'proxy copy')])),
            ],
            options={
                'verbose_name': 'Project',
            },
        ),
        migrations.CreateModel(
            name='projectListType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectInfo', models.ManyToManyField(related_name='projectInfo_projectlisttype_model_related', verbose_name=b'Project', to='repository.projectInfoType_model')),
            ],
            options={
                'verbose_name': 'Project list',
            },
        ),
        migrations.CreateModel(
            name='recordingInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recordingDeviceType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The nature of the recording platform hardware and the storage medium', max_length=2, verbose_name=b'Recording device type', choices=[('hardDisk', 'Hard Disk'), ('dv', 'Dv'), ('tapeVHS', 'TapeVHS'), ('flash', 'Flash'), ('DAT', 'DAT'), ('soundBlasterCard', 'Sound Blaster Card'), ('other', 'Other')])),
                ('recordingDeviceTypeDetails', metashare.repository.fields.XmlCharField(help_text=b'Free text description of the recoding device', max_length=500, verbose_name=b'Recording device type details', blank=True)),
                ('recordingPlatformSoftware', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The software used for the recording platform', max_length=100, verbose_name=b'Recording platform software', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('recordingEnvironment', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Where the recording took place', max_length=3, verbose_name=b'Recording environment', choices=[('office', 'Office'), ('inCar', 'In Car'), ('studio', 'Studio'), ('conferenceRoom', 'Conference Room'), ('lectureRoom', 'Lecture Room'), ('industrial', 'Industrial'), ('transport', 'Transport'), ('openPublicPlace', 'Open Public Place'), ('closedPublicPlace', 'Closed Public Place'), ('anechoicChamber', 'Anechoic Chamber'), ('other', 'Other')])),
                ('sourceChannel', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Information on the source channel', max_length=3, verbose_name=b'Source channel', choices=[('internet', 'Internet'), ('radio', 'Radio'), ('tv', 'Tv'), ('telephone', 'Telephone'), ('laryngograph', 'Laryngograph'), ('airflow', 'Airflow'), ('EMA', 'EMA'), ('webCam', 'Web Cam'), ('camcorder', 'Camcorder'), ('other', 'Other')])),
                ('sourceChannelType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Type of the source channel', max_length=3, verbose_name=b'Source channel type', choices=[('ISDN', 'ISDN'), ('GSM', 'GSM'), ('3G', '3G'), ('CDMA', 'CDMA'), ('DVB-T', 'DVB - T'), ('DVB-S', 'DVB - S'), ('DVB-C', 'DVB - C'), ('VOIP', 'VOIP'), ('other', 'Other')])),
                ('sourceChannelName', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The name of the specific source recorded', max_length=30, verbose_name=b'Source channel name', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('sourceChannelDetails', metashare.repository.fields.XmlCharField(help_text=b'The details of the channel equipment used (brand, type etc.)', max_length=200, verbose_name=b'Source channel details', blank=True)),
            ],
            options={
                'verbose_name': 'Recording',
            },
        ),
        migrations.CreateModel(
            name='relatedLexiconInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relatedLexiconType', models.CharField(help_text=b'Indicates the position of the lexica that must or can be used with the grammar', max_length=30, verbose_name=b'Related lexicon type', choices=[('attached', 'Attached'), ('compatible', 'Compatible'), ('included', 'Included'), ('none', 'None')])),
                ('attachedLexiconPosition', metashare.repository.fields.XmlCharField(help_text=b'Indicates the position of the lexicon, if attached to the grammar', max_length=500, verbose_name=b'Attached lexicon position', blank=True)),
                ('compatibleLexiconType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Type of (external) lexicon that can be used with the grammar', max_length=2, verbose_name=b'Compatible lexicon type', choices=[('wordnet', 'Wordnet'), ('wordlist', 'Wordlist'), ('morphologicalLexicon', 'Morphological Lexicon'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Related lexicon',
            },
        ),
        migrations.CreateModel(
            name='relationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relationType', metashare.repository.fields.XmlCharField(help_text=b'Specifies the type of relation not covered by the ones proposed by META-SHARE', max_length=100, verbose_name=b'Relation type')),
            ],
            options={
                'verbose_name': 'Relation',
            },
        ),
        migrations.CreateModel(
            name='resolutionInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sizeWidth', models.IntegerField(help_text=b'The frame width in pixels', null=True, verbose_name=b'Size width', blank=True)),
                ('sizeHeight', models.IntegerField(help_text=b'The frame height in pixels', null=True, verbose_name=b'Size height', blank=True)),
                ('resolutionStandard', models.CharField(blank=True, help_text=b'The standard to which the resolution conforms', max_length=50, verbose_name=b'Resolution standard', choices=[('HD.1080', 'HD.1080'), ('HD.720', 'HD.720'), ('VGA', 'VGA')])),
            ],
            options={
                'verbose_name': 'Resolution',
            },
        ),
        migrations.CreateModel(
            name='resourceComponentTypeType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Resource component',
            },
        ),
        migrations.CreateModel(
            name='resourceCreationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creationStartDate', models.DateField(help_text=b'The date in which the creation process was started', null=True, verbose_name=b'Creation start date', blank=True)),
                ('creationEndDate', models.DateField(help_text=b'The date in which the creation process was completed', null=True, verbose_name=b'Creation end date', blank=True)),
                ('fundingProject', models.ManyToManyField(related_name='fundingProject_resourcecreationinfotype_model_related', to='repository.projectInfoType_model', blank=True, help_text=b'Groups information on the project that has funded the resource', null=True, verbose_name=b'Funding project')),
            ],
            options={
                'verbose_name': 'Resource creation',
            },
        ),
        migrations.CreateModel(
            name='resourceDocumentationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('samplesLocation', metashare.repository.fields.MultiTextField(blank=True, help_text=b'A url with samples of the resource or, in the case of tools, of samples of the output', max_length=1000, verbose_name=b'Samples location', validators=[django.core.validators.RegexValidator(b"^(?i)((http|ftp)s?):\\/\\/(([a-z0-9.-]|%[0-9A-F]{2}){3,})(:(\\d+))?((\\/([a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(\\?(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(#(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(?!\\r?\\n)$", b'Not a valid URL value (must not contain non-ASCII characters, for example; see also RFC 2396).', django.core.exceptions.ValidationError)])),
                ('toolDocumentationType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Specifies the type of documentation for tool or service', max_length=2, verbose_name=b'Tool documentation', choices=[('online', 'Online'), ('manual', 'Manual'), ('helpFunctions', 'Help Functions'), ('none', 'None'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Resource documentation',
            },
        ),
        migrations.CreateModel(
            name='resourceInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distributionInfo', models.OneToOneField(verbose_name=b'Distribution', to='repository.distributionInfoType_model', help_text=b'Groups information on the distribution of the resource')),
                ('editor_groups', models.ManyToManyField(to='accounts.EditorGroup', blank=True)),
                ('identificationInfo', models.OneToOneField(verbose_name=b'Identification', to='repository.identificationInfoType_model', help_text=b'Groups together information needed to identify the resource')),
                ('metadataInfo', models.OneToOneField(verbose_name=b'Metadata', to='repository.metadataInfoType_model', help_text=b'Groups information on the metadata record itself')),
                ('owners', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': 'Resource',
            },
        ),
        migrations.CreateModel(
            name='runningEnvironmentInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('requiredHardware', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Hardware required for running a tool and/or computational grammar', max_length=2, verbose_name=b'Required hardware', choices=[('graphicCard', 'Graphic Card'), ('microphone', 'Microphone'), ('ocrSystem', 'Ocr System'), ('specialHardwareEquipment', 'Special Hardware Equipment'), ('none', 'None'), ('other', 'Other')])),
                ('runningEnvironmentDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on the running environment', max_length=200, verbose_name=b'Running environment details', blank=True)),
            ],
            options={
                'verbose_name': 'Running environment',
            },
        ),
        migrations.CreateModel(
            name='settingInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('naturality', models.CharField(blank=True, help_text=b'Specifies the level of naturality for multimodal/multimedia resources', max_length=30, verbose_name=b'Naturality', choices=[('assisted', 'Assisted'), ('elicited', 'Elicited'), ('natural', 'Natural'), ('other', 'Other'), ('planned', 'Planned'), ('prompted', 'Prompted'), ('readSpeech', 'Read Speech'), ('semiPlanned', 'Semi Planned'), ('spontaneous', 'Spontaneous')])),
                ('conversationalType', models.CharField(blank=True, help_text=b'Specifies the conversational type of the resource', max_length=30, verbose_name=b'Conversational type', choices=[('dialogue', 'Dialogue'), ('monologue', 'Monologue'), ('multilogue', 'Multilogue')])),
                ('scenarioType', models.CharField(blank=True, help_text=b'Indicates the task defined for the conversation or the interaction of participants', max_length=30, verbose_name=b'Scenario type', choices=[('frogStory', 'Frog Story'), ('mapTask', 'Map Task'), ('onlineEducationalGame', 'Online Educational Game'), ('other', 'Other'), ('pearStory', 'Pear Story'), ('pearStory', 'Pear Story'), ('rolePlay', 'Role Play'), ('wizardOfOz', 'Wizard Of Oz'), ('wordGame', 'Word Game')])),
                ('audience', models.CharField(blank=True, help_text=b'Indication of the intended audience size', max_length=30, verbose_name=b'Audience', choices=[('few', 'Few'), ('largePublic', 'Large Public'), ('no', 'No'), ('some', 'Some')])),
                ('interactivity', models.CharField(blank=True, help_text=b'Indicates the level of conversational interaction between speakers (for audio component) or participants (for video component)', max_length=30, verbose_name=b'Interactivity', choices=[('interactive', 'Interactive'), ('nonInteractive', 'Non Interactive'), ('other', 'Other'), ('overlapping', 'Overlapping'), ('semiInteractive', 'Semi Interactive')])),
                ('interaction', metashare.repository.fields.XmlCharField(help_text=b'Specifies the parts that interact in an audio or video component', max_length=1000, verbose_name=b'Interaction', blank=True)),
            ],
            options={
                'verbose_name': 'Setting',
            },
        ),
        migrations.CreateModel(
            name='sizeInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', metashare.repository.fields.XmlCharField(help_text=b'Specifies the size of the resource with regard to the SizeUnit measurement in form of a number', max_length=100, verbose_name=b'Size')),
                ('sizeUnit', models.CharField(help_text=b'Specifies the unit that is used when providing information on the size of the resource or of resource parts', max_length=30, verbose_name=b'Size unit', choices=[('4-grams', '4 - Grams'), ('5-grams', '5 - Grams'), ('articles', 'Articles'), ('bigrams', 'Bigrams'), ('bytes', 'Bytes'), ('classes', 'Classes'), ('concepts', 'Concepts'), ('diphones', 'Diphones'), ('elements', 'Elements'), ('entries', 'Entries'), ('expressions', 'Expressions'), ('files', 'Files'), ('frames', 'Frames'), ('gb', 'Gb'), ('hours', 'Hours'), ('idiomaticExpressions', 'Idiomatic Expressions'), ('images', 'Images'), ('items', 'Items'), ('kb', 'Kb'), ('keywords', 'Keywords'), ('lexicalTypes', 'Lexical Types'), ('mb', 'Mb'), ('minutes', 'Minutes'), ('multiWordUnits', 'Multi Word Units'), ('neologisms', 'Neologisms'), ('other', 'Other'), ('phonemes', 'Phonemes'), ('phoneticUnits', 'Phonetic Units'), ('predicates', 'Predicates'), ('questions', 'Questions'), ('rb', 'Rb'), ('rules', 'Rules'), ('seconds', 'Seconds'), ('semanticUnits', 'Semantic Units'), ('sentences', 'Sentences'), ('shots', 'Shots'), ('syllables', 'Syllables'), ('synsets', 'Synsets'), ('syntacticUnits', 'Syntactic Units'), ('T-HPairs', 'T - H Pairs'), ('terms', 'Terms'), ('texts', 'Texts'), ('tokens', 'Tokens'), ('trigrams', 'Trigrams'), ('turns', 'Turns'), ('unigrams', 'Unigrams'), ('units', 'Units'), ('utterances', 'Utterances'), ('words', 'Words')])),
                ('back_to_audiosizeinfotype_model', models.ForeignKey(blank=True, to='repository.audioSizeInfoType_model', null=True)),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextngraminfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True)),
                ('back_to_corpustextnumericalinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNumericalInfoType_model', null=True)),
                ('back_to_corpusvideoinfotype_model', models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True)),
                ('back_to_languagedescriptionimageinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionImageInfoType_model', null=True)),
                ('back_to_languagedescriptiontextinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionTextInfoType_model', null=True)),
                ('back_to_languagedescriptionvideoinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionVideoInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourceaudioinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceAudioInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourceimageinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceImageInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourcetextinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceTextInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourcevideoinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceVideoInfoType_model', null=True)),
            ],
            options={
                'verbose_name': 'Size',
            },
        ),
        migrations.CreateModel(
            name='staticElementInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfElement', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The type of objects or people that represented in the video or image part of the resource', max_length=1000, verbose_name=b'Type of element', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('bodyParts', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'The body parts visible in the video or image part of the resource', max_length=3, verbose_name=b'Body parts', choices=[('arms', 'Arms'), ('face', 'Face'), ('feet', 'Feet'), ('hands', 'Hands'), ('head', 'Head'), ('legs', 'Legs'), ('mouth', 'Mouth'), ('wholeBody', 'Whole Body'), ('none', 'None')])),
                ('faceViews', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the view of the face(s) that appear in the video or on the image part of the resource', max_length=1000, verbose_name=b'Face views', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('faceExpressions', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the facial expressions visible in the resource', max_length=1000, verbose_name=b'Face expressions', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('artifactParts', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Indicates the parts of the artifacts represented in the image corpus', max_length=1000, verbose_name=b'Artifact parts', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('landscapeParts', metashare.repository.fields.MultiTextField(blank=True, help_text=b'landscape parts represented in the image corpus', max_length=1000, verbose_name=b'Landscape parts', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('personDescription', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Provides descriptive features for the persons represented in the image corpus', max_length=1000, verbose_name=b'Person description', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('thingDescription', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Provides description of the things represented in the image corpus', max_length=1000, verbose_name=b'Thing description', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('organizationDescription', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Provides description of the organizations that may appear in the image corpus', max_length=1000, verbose_name=b'Organization description', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('eventDescription', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Provides description of any events represented in the image corpus', max_length=1000, verbose_name=b'Event description', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
            ],
            options={
                'verbose_name': 'Static element',
            },
        ),
        migrations.CreateModel(
            name='targetResourceInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('targetResourceNameURI', metashare.repository.fields.XmlCharField(help_text=b'The full name or a url to a resource related to the one being described; to be used for identifiers also for this version', max_length=4500, verbose_name=b'Target resource name uri')),
            ],
            options={
                'verbose_name': 'Target resource',
            },
        ),
        migrations.CreateModel(
            name='textClassificationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('textGenre', metashare.repository.fields.XmlCharField(help_text=b'Genre: The conventionalized discourse or text types of the content of the resource, based on extra-linguistic and internal linguistic criteria', max_length=50, verbose_name=b'Text genre', blank=True)),
                ('textType', metashare.repository.fields.XmlCharField(help_text=b'Specifies the type of the text according to a text type classification', max_length=50, verbose_name=b'Text type', blank=True)),
                ('register', metashare.repository.fields.XmlCharField(help_text=b'For corpora that have already been using register classification', max_length=500, verbose_name=b'Register', blank=True)),
                ('subject_topic', metashare.repository.fields.XmlCharField(help_text=b'For corpora that have already been using subject classification', max_length=500, verbose_name=b'Subject topic', blank=True)),
                ('conformanceToClassificationScheme', models.CharField(blank=True, help_text=b'Specifies the external classification schemes', max_length=100, verbose_name=b'Conformance to classification scheme', choices=[('ANC_domainClassification', 'ANC_domain Classification'), ('ANC_genreClassification', 'ANC_genre Classification'), ('BNC_domainClassification', 'BNC_domain Classification'), ('BNC_textTypeClassification', 'BNC_text Type Classification'), ('DDC_classification', 'DDC_classification'), ('libraryOfCongress_domainClassification', 'Library Of Congress_domain Classification'), ('libraryofCongressSubjectHeadings_classification', 'Libraryof Congress Subject Headings_classification'), ('MeSH_classification', 'MeSH_classification'), ('NLK_classification', 'NLK_classification'), ('other', 'Other'), ('PAROLE_genreClassification', 'PAROLE_genre Classification'), ('PAROLE_topicClassification', 'PAROLE_topic Classification'), ('UDC_classification', 'UDC_classification')])),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextngraminfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True)),
                ('sizePerTextClassification', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on size of resource parts with different text classification', verbose_name=b'Size per text classification')),
            ],
            options={
                'verbose_name': 'Text classification',
            },
        ),
        migrations.CreateModel(
            name='textFormatInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mimeType', metashare.repository.fields.XmlCharField(help_text=b'The mime-type of the resource which is a formalized specifier for the format included or a mime-type that the tool/service accepts; value to be taken from a subset of the official mime types of the Internet Assigned Numbers Authority (http://www.iana.org/)', max_length=50, verbose_name=b'Mime type')),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextngraminfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True)),
                ('back_to_languagedescriptiontextinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionTextInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourcetextinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceTextInfoType_model', null=True)),
                ('sizePerTextFormat', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on the size of the resource parts with different format', verbose_name=b'Size per text format')),
            ],
            options={
                'verbose_name': 'Text format',
            },
        ),
        migrations.CreateModel(
            name='textNumericalContentInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfTextNumericalContent', metashare.repository.fields.MultiTextField(help_text=b'Specifies the content that is represented in the textNumerical part of the resource', max_length=1000, verbose_name=b'Type of text numerical content', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
            ],
            options={
                'verbose_name': 'Text numerical content',
            },
        ),
        migrations.CreateModel(
            name='textNumericalFormatInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mimeType', metashare.repository.fields.XmlCharField(help_text=b'The mime-type of the resource which is a formalized specifier for the format included or a mime-type that the tool/service accepts; value to be taken from a subset of the official mime types of the Internet Assigned Numbers Authority (http://www.iana.org/)', max_length=1000, verbose_name=b'Mime type')),
                ('back_to_corpustextnumericalinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNumericalInfoType_model', null=True)),
                ('sizePerTextNumericalFormat', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Gives information on the size of textNumerical resource parts with different format', verbose_name=b'Size per text numerical format')),
            ],
            options={
                'verbose_name': 'Text numerical format',
            },
        ),
        migrations.CreateModel(
            name='timeCoverageInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeCoverage', metashare.repository.fields.XmlCharField(help_text=b'The time period that the content of a resource is about', max_length=100, verbose_name=b'Time coverage')),
                ('back_to_corpusaudioinfotype_model', models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True)),
                ('back_to_corpusimageinfotype_model', models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True)),
                ('back_to_corpustextinfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True)),
                ('back_to_corpustextngraminfotype_model', models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True)),
                ('back_to_corpusvideoinfotype_model', models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True)),
                ('back_to_languagedescriptionimageinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionImageInfoType_model', null=True)),
                ('back_to_languagedescriptiontextinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionTextInfoType_model', null=True)),
                ('back_to_languagedescriptionvideoinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionVideoInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourceaudioinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceAudioInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourceimageinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceImageInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourcetextinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceTextInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourcevideoinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceVideoInfoType_model', null=True)),
                ('sizePerTimeCoverage', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on size per time period represented in the resource', verbose_name=b'Size per time coverage')),
            ],
            options={
                'verbose_name': 'Time coverage',
            },
        ),
        migrations.CreateModel(
            name='toolServiceCreationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('implementationLanguage', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The programming languages needed for allowing user contributions, or for running the tools, in case no executables are available', max_length=100, verbose_name=b'Implementation language', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('formalism', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Reference (name, bibliographic reference or link to url) for the formalism used for the creation/enrichment of the resource (grammar or tool/service)', max_length=100, verbose_name=b'Formalism', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('creationDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides additional information on the creation of a tool or service', max_length=500, verbose_name=b'Creation details', blank=True)),
                ('originalSource', models.ManyToManyField(related_name='originalSource_toolservicecreationinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'The name, the identifier or the url of thethe original resources that were at the base of the creation process of the resource', null=True, verbose_name=b'Original source')),
            ],
            options={
                'verbose_name': 'Tool service creation',
            },
        ),
        migrations.CreateModel(
            name='toolServiceEvaluationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluated', metashare.repository.fields.MetaBooleanField(help_text=b'Indicates whether the tool or service has been evaluated', verbose_name=b'Evaluated', choices=[(True, b'Yes'), (False, b'No')])),
                ('evaluationLevel', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Indicates the evaluation level', max_length=2, verbose_name=b'Evaluation level', choices=[('technological', 'Technological'), ('usage', 'Usage'), ('impact', 'Impact'), ('diagnostic', 'Diagnostic')])),
                ('evaluationType', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Indicates the evaluation type', max_length=1, verbose_name=b'Evaluation type', choices=[('glassBox', 'Glass Box'), ('blackBox', 'Black Box')])),
                ('evaluationCriteria', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Defines the criteria of the evaluation of a tool', max_length=1, verbose_name=b'Evaluation criteria', choices=[('extrinsic', 'Extrinsic'), ('intrinsic', 'Intrinsic')])),
                ('evaluationMeasure', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Defines whether the evaluation measure is human or automatic', max_length=1, verbose_name=b'Evaluation measure', choices=[('human', 'Human'), ('automatic', 'Automatic')])),
                ('evaluationDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides further information on the evaluation process of a tool or service', max_length=500, verbose_name=b'Evaluation details', blank=True)),
            ],
            options={
                'verbose_name': 'Tool service evaluation',
            },
        ),
        migrations.CreateModel(
            name='toolServiceOperationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operatingSystem', metashare.repository.fields.MultiSelectField(help_text=b'The operating system on which the tool will be running', max_length=2, verbose_name=b'Operating system', choices=[('os-independent', 'Os - Independent'), ('windows', 'Windows'), ('linux', 'Linux'), ('unix', 'Unix'), ('mac-OS', 'Mac - OS'), ('other', 'Other')])),
                ('runningTime', metashare.repository.fields.XmlCharField(help_text=b'Gives information on the running time of a tool or service', max_length=100, verbose_name=b'Running time', blank=True)),
                ('runningEnvironmentInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.runningEnvironmentInfoType_model', blank=True, help_text=b'Groups together information on the running environment of a tool or a language description', verbose_name=b'Running environment')),
            ],
            options={
                'verbose_name': 'Tool service operation',
            },
        ),
        migrations.CreateModel(
            name='usageInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accessTool', models.ManyToManyField(related_name='accessTool_usageinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'The name or the identifier or the url of the tool used to access a resource (e.g. a corpus workbench)', null=True, verbose_name=b'Access tool')),
                ('resourceAssociatedWith', models.ManyToManyField(related_name='resourceAssociatedWith_usageinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'Refers to another resource that the resource described uses for its operation', null=True, verbose_name=b'Resource associated with')),
            ],
            options={
                'verbose_name': 'Usage',
            },
        ),
        migrations.CreateModel(
            name='validationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('validated', metashare.repository.fields.MetaBooleanField(help_text=b'Specifies the validation status of the resource', verbose_name=b'Validated', choices=[(True, b'Yes'), (False, b'No')])),
                ('validationType', models.CharField(blank=True, help_text=b'Specifies the type of the validation that have been performed', max_length=20, verbose_name=b'Validation type', choices=[('content', 'Content'), ('formal', 'Formal')])),
                ('validationMode', models.CharField(blank=True, help_text=b'Specifies the validation methodology applied', max_length=20, verbose_name=b'Validation mode', choices=[('automatic', 'Automatic'), ('interactive', 'Interactive'), ('manual', 'Manual'), ('mixed', 'Mixed')])),
                ('validationModeDetails', metashare.repository.fields.XmlCharField(help_text=b'Textual field for additional information on validation', max_length=500, verbose_name=b'Validation mode details', blank=True)),
                ('validationExtent', models.CharField(blank=True, help_text=b'The resource coverage in terms of validated data', max_length=20, verbose_name=b'Validation extent', choices=[('full', 'Full'), ('partial', 'Partial')])),
                ('validationExtentDetails', metashare.repository.fields.XmlCharField(help_text=b'Provides information on size or other details of partially validated data; to be used if only part of the resource has been validated and as an alternative to SizeInfo if the validated part cannot be counted otherwise', max_length=500, verbose_name=b'Validation extent details', blank=True)),
                ('back_to_resourceinfotype_model', models.ForeignKey(blank=True, to='repository.resourceInfoType_model', null=True)),
                ('sizePerValidation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Specifies the size of the validated part of a resource', verbose_name=b'Size per validation')),
            ],
            options={
                'verbose_name': 'Validation',
            },
        ),
        migrations.CreateModel(
            name='versionInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', metashare.repository.fields.XmlCharField(help_text=b'Any string, usually a number, that identifies the version of a resource', max_length=100, verbose_name=b'Version')),
                ('revision', metashare.repository.fields.XmlCharField(help_text=b'Provides an account of the revisions in free text or a link to a document with revisions', max_length=500, verbose_name=b'Revision', blank=True)),
                ('lastDateUpdated', models.DateField(help_text=b'Date of the last update of the version of the resource', null=True, verbose_name=b'Last date updated', blank=True)),
                ('updateFrequency', metashare.repository.fields.XmlCharField(help_text=b'Specifies the frequency with which the resource is updated', max_length=100, verbose_name=b'Update frequency', blank=True)),
            ],
            options={
                'verbose_name': 'Version',
            },
        ),
        migrations.CreateModel(
            name='videoClassificationInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('videoGenre', metashare.repository.fields.XmlCharField(help_text=b'A first indication of type of video recorded', max_length=1000, verbose_name=b'Video genre', blank=True)),
                ('subject_topic', metashare.repository.fields.XmlCharField(help_text=b'For corpora that have already been using subject classification', max_length=1000, verbose_name=b'Subject topic', blank=True)),
                ('conformanceToClassificationScheme', models.CharField(blank=True, help_text=b'Specifies the external classification schemes', max_length=100, verbose_name=b'Conformance to classification scheme', choices=[('ANC_domainClassification', 'ANC_domain Classification'), ('ANC_genreClassification', 'ANC_genre Classification'), ('BNC_domainClassification', 'BNC_domain Classification'), ('BNC_textTypeClassification', 'BNC_text Type Classification'), ('DDC_classification', 'DDC_classification'), ('libraryOfCongress_domainClassification', 'Library Of Congress_domain Classification'), ('libraryofCongressSubjectHeadings_classification', 'Libraryof Congress Subject Headings_classification'), ('MeSH_classification', 'MeSH_classification'), ('NLK_classification', 'NLK_classification'), ('other', 'Other'), ('PAROLE_genreClassification', 'PAROLE_genre Classification'), ('PAROLE_topicClassification', 'PAROLE_topic Classification'), ('UDC_classification', 'UDC_classification')])),
                ('back_to_corpusvideoinfotype_model', models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True)),
                ('sizePerVideoClassification', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Used to give info on size of parts with different video classification', verbose_name=b'Size per video classification')),
            ],
            options={
                'verbose_name': 'Video classification',
            },
        ),
        migrations.CreateModel(
            name='videoContentInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfVideoContent', metashare.repository.fields.MultiTextField(help_text=b'Main type of object or people represented in the video', max_length=1000, verbose_name=b'Type of video content', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('textIncludedInVideo', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Indicates if text is present in or in conjunction with the video', max_length=1, verbose_name=b'Text included in video', choices=[('captions', 'Captions'), ('subtitles', 'Subtitles'), ('none', 'None')])),
                ('dynamicElementInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.dynamicElementInfoType_model', blank=True, help_text=b'Groups information on the dynamic elements that are represented in the video part of the resource', verbose_name=b'Dynamic element')),
            ],
            options={
                'verbose_name': 'Video content',
            },
        ),
        migrations.CreateModel(
            name='videoFormatInfoType_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mimeType', metashare.repository.fields.XmlCharField(help_text=b'The mime-type of the resource which is a formalized specifier for the format included or a mime-type that the tool/service accepts; value to be taken from a subset of the official mime types of the Internet Assigned Numbers Authority (http://www.iana.org/)', max_length=50, verbose_name=b'Mime type')),
                ('colourSpace', metashare.repository.fields.MultiSelectField(blank=True, help_text=b'Defines the colour space for the video', max_length=2, verbose_name=b'Colour space', choices=[('RGB', 'RGB'), ('CMYK', 'CMYK'), ('4:2:2', '4:2:2'), ('YUV', 'YUV')])),
                ('colourDepth', models.IntegerField(help_text=b'The number of bits used to represent the colour of a single pixel', null=True, verbose_name=b'Colour depth', blank=True)),
                ('frameRate', models.IntegerField(help_text=b'The number of frames per second', null=True, verbose_name=b'Frame rate', blank=True)),
                ('visualModelling', models.CharField(blank=True, help_text=b'The dimensional form applied on video or image corpus', max_length=30, verbose_name=b'Visual modelling', choices=[('2D', '2D'), ('3D', '3D')])),
                ('fidelity', metashare.repository.fields.MetaBooleanField(help_text=b'Defines whether blur is present in the moving sequences', verbose_name=b'Fidelity', choices=[(True, b'Yes'), (False, b'No')])),
                ('back_to_corpusvideoinfotype_model', models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True)),
                ('back_to_languagedescriptionvideoinfotype_model', models.ForeignKey(blank=True, to='repository.languageDescriptionVideoInfoType_model', null=True)),
                ('back_to_lexicalconceptualresourcevideoinfotype_model', models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceVideoInfoType_model', null=True)),
                ('compressionInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.compressionInfoType_model', blank=True, help_text=b'Groups together information on the compression status and method of a resource', verbose_name=b'Compression')),
                ('resolutionInfo', models.ManyToManyField(related_name='resolutionInfo_videoformatinfotype_model_related', to='repository.resolutionInfoType_model', blank=True, help_text=b'Groups together information on the image resolution', null=True, verbose_name=b'Resolution')),
                ('sizePerVideoFormat', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Used to give info on size of parts of a resource that differ as to the format', verbose_name=b'Size per video format')),
            ],
            options={
                'verbose_name': 'Video format',
            },
        ),
        migrations.CreateModel(
            name='corpusInfoType_model',
            fields=[
                ('resourcecomponenttypetype_model_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='repository.resourceComponentTypeType_model')),
                ('resourceType', metashare.repository.fields.XmlCharField(default=b'corpus', help_text=b'Specifies the type of the resource being described', max_length=1000, editable=False, verbose_name=b'Resource')),
            ],
            options={
                'verbose_name': 'Corpus',
            },
            bases=('repository.resourcecomponenttypetype_model',),
        ),
        migrations.CreateModel(
            name='documentInfoType_model',
            fields=[
                ('documentationinfotype_model_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='repository.documentationInfoType_model')),
                ('documentType', models.CharField(help_text=b'Specifies the type of the document provided with or related to the resource', max_length=30, verbose_name=b'Document', choices=[('article', 'Article'), ('book', 'Book'), ('booklet', 'Booklet'), ('inBook', 'In Book'), ('inCollection', 'In Collection'), ('inProceedings', 'In Proceedings'), ('manual', 'Manual'), ('mastersThesis', 'Masters Thesis'), ('other', 'Other'), ('phdThesis', 'Phd Thesis'), ('proceedings', 'Proceedings'), ('techReport', 'Tech Report'), ('unpublished', 'Unpublished')])),
                ('title', metashare.repository.fields.DictField(help_text=b'The title of the document reporting on the resource', null=True, verbose_name=b'Title', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('author', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The name(s) of the author(s), in the format described in the document', max_length=1000, verbose_name=b'Author', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('editor', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The name of the editor as mentioned in the document', max_length=200, verbose_name=b'Editor', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('year', metashare.repository.fields.XmlCharField(blank=True, help_text=b'The year of publication or, for an unpublished work, the year it was written', max_length=1000, verbose_name=b'Year', validators=[metashare.repository.validators.validate_xml_schema_year])),
                ('publisher', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The name of the publisher', max_length=200, verbose_name=b'Publisher', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('bookTitle', metashare.repository.fields.XmlCharField(help_text=b'The title of a book, part of which is being cited', max_length=200, verbose_name=b'Book title', blank=True)),
                ('journal', metashare.repository.fields.XmlCharField(help_text=b'A journal name. Abbreviations could also be provided', max_length=200, verbose_name=b'Journal', blank=True)),
                ('volume', metashare.repository.fields.XmlCharField(help_text=b'Specifies the volume of a journal or multivolume book', max_length=1000, verbose_name=b'Volume', blank=True)),
                ('series', metashare.repository.fields.XmlCharField(help_text=b'The name of a series or set of books. When citing an entire book, the title field gives its title and an optional series field gives the name of a series or multi-volume set in which the book is published', max_length=200, verbose_name=b'Series', blank=True)),
                ('pages', metashare.repository.fields.XmlCharField(help_text=b'One or more page numbers or range of page numbers', max_length=100, verbose_name=b'Pages', blank=True)),
                ('edition', metashare.repository.fields.XmlCharField(help_text=b'The edition of a book', max_length=100, verbose_name=b'Edition', blank=True)),
                ('conference', metashare.repository.fields.XmlCharField(help_text=b'The name of the conference in which the document has been presented', max_length=300, verbose_name=b'Conference', blank=True)),
                ('doi', metashare.repository.fields.XmlCharField(help_text=b'A digital object identifier assigned to the document', max_length=100, verbose_name=b'Doi', blank=True)),
                ('url', metashare.repository.fields.XmlCharField(blank=True, help_text=b'A URL used as homepage of an entity (e.g. of a person, organization, resource etc.) and/or where an entity (e.g.LR, document etc.) is located', max_length=1000, verbose_name=b'Url', validators=[django.core.validators.RegexValidator(b"^(?i)((http|ftp)s?):\\/\\/(([a-z0-9.-]|%[0-9A-F]{2}){3,})(:(\\d+))?((\\/([a-z0-9-._~!$&'()*+,;=:@]|%[0-9A-F]{2})*)*)(\\?(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(#(([a-z0-9-._~!$&'()*+,;=:\\/?@]|%[0-9A-F]{2})*))?(?!\\r?\\n)$", b'Not a valid URL value (must not contain non-ASCII characters, for example; see also RFC 2396).', django.core.exceptions.ValidationError)])),
                ('ISSN', metashare.repository.fields.XmlCharField(help_text=b'The International Standard Serial Number used to identify a journal', max_length=100, verbose_name=b'Issn', blank=True)),
                ('ISBN', metashare.repository.fields.XmlCharField(help_text=b'The International Standard Book Number', max_length=100, verbose_name=b'Isbn', blank=True)),
                ('keywords', metashare.repository.fields.MultiTextField(blank=True, help_text=b'The keyword(s) for indexing and classification of the document', max_length=250, verbose_name=b'Keywords', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('documentLanguageName', metashare.repository.fields.XmlCharField(help_text=b'The name of the language the document is written in; an autocompletion mechanism with values from the ISO 639 is provided in the editor, but the values can be subsequently edited for further specification (according to the IETF BCP47 guidelines)', max_length=150, verbose_name=b'Document language name', blank=True)),
                ('documentLanguageId', metashare.repository.fields.XmlCharField(help_text=b'The id of the language the document is written in; an autocompletion mechanism with values from the ISO 639 is provided in the editor, but the values can be subsequently edited for further specification (according to the IETF BCP47 guidelines)', max_length=20, verbose_name=b'Document language id', blank=True)),
                ('source_url', models.URLField(default=b'http://127.0.0.1:8000', help_text=b'(Read-only) base URL for the server where the master copy of the associated entity instance is located.')),
                ('copy_status', models.CharField(default=b'm', help_text=b'Generalized copy status flag for this entity instance.', max_length=1, choices=[(b'm', b'master copy'), (b'r', b'remote copy'), (b'p', b'proxy copy')])),
            ],
            options={
                'verbose_name': 'Document',
            },
            bases=('repository.documentationinfotype_model',),
        ),
        migrations.CreateModel(
            name='documentUnstructuredString_model',
            fields=[
                ('documentationinfotype_model_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='repository.documentationInfoType_model')),
                ('invisiblestringmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='repository.InvisibleStringModel')),
            ],
            options={
                'abstract': False,
            },
            bases=('repository.invisiblestringmodel', 'repository.documentationinfotype_model'),
        ),
        migrations.CreateModel(
            name='languageDescriptionInfoType_model',
            fields=[
                ('resourcecomponenttypetype_model_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='repository.resourceComponentTypeType_model')),
                ('resourceType', metashare.repository.fields.XmlCharField(default=b'languageDescription', help_text=b'Specifies the type of the resource being described', max_length=30, editable=False, verbose_name=b'Resource')),
                ('languageDescriptionType', models.CharField(help_text=b'The type of the language description', max_length=30, verbose_name=b'Language description type', choices=[('grammar', 'Grammar'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Language description',
            },
            bases=('repository.resourcecomponenttypetype_model',),
        ),
        migrations.CreateModel(
            name='lexicalConceptualResourceInfoType_model',
            fields=[
                ('resourcecomponenttypetype_model_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='repository.resourceComponentTypeType_model')),
                ('resourceType', metashare.repository.fields.XmlCharField(default=b'lexicalConceptualResource', help_text=b'Specifies the type of the resource being described', max_length=1000, editable=False, verbose_name=b'Resource')),
                ('lexicalConceptualResourceType', models.CharField(help_text=b'Specifies the subtype of lexicalConceptualResource', max_length=25, verbose_name=b'Lexical conceptual resource type', choices=[('wordList', 'Word List'), ('computationalLexicon', 'Computational Lexicon'), ('ontology', 'Ontology'), ('wordnet', 'Wordnet'), ('thesaurus', 'Thesaurus'), ('framenet', 'Framenet'), ('terminologicalResource', 'Terminological Resource'), ('machineReadableDictionary', 'Machine Readable Dictionary'), ('lexicon', 'Lexicon'), ('other', 'Other')])),
            ],
            options={
                'verbose_name': 'Lexical conceptual resource',
            },
            bases=('repository.resourcecomponenttypetype_model',),
        ),
        migrations.CreateModel(
            name='organizationInfoType_model',
            fields=[
                ('actorinfotype_model_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='repository.actorInfoType_model')),
                ('organizationName', metashare.repository.fields.DictField(help_text=b'The full name of an organization', null=True, verbose_name=b'Organization name', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('organizationShortName', metashare.repository.fields.DictField(blank=True, help_text=b'The short name (abbreviation, acronym etc.) used for an organization', null=True, verbose_name=b'Organization short name', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('departmentName', metashare.repository.fields.DictField(blank=True, help_text=b'The name of the department or unit (e.g. specific university faculty/department, department/unit of a research organization or private company etc.)', null=True, verbose_name=b'Department name', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('source_url', models.URLField(default=b'http://127.0.0.1:8000', help_text=b'(Read-only) base URL for the server where the master copy of the associated entity instance is located.')),
                ('copy_status', models.CharField(default=b'm', help_text=b'Generalized copy status flag for this entity instance.', max_length=1, choices=[(b'm', b'master copy'), (b'r', b'remote copy'), (b'p', b'proxy copy')])),
                ('communicationInfo', models.OneToOneField(verbose_name=b'Communication', to='repository.communicationInfoType_model', help_text=b'Groups information on communication details of a person or an organization')),
            ],
            options={
                'verbose_name': 'Organization',
            },
            bases=('repository.actorinfotype_model',),
        ),
        migrations.CreateModel(
            name='personInfoType_model',
            fields=[
                ('actorinfotype_model_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='repository.actorInfoType_model')),
                ('surname', metashare.repository.fields.DictField(help_text=b'The surname (family name) of a person related to the resource', null=True, verbose_name=b'Surname', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('givenName', metashare.repository.fields.DictField(blank=True, help_text=b'The given name (first name) of a person related to the resource; initials can also be used', null=True, verbose_name=b'Given name', validators=[metashare.repository.validators.validate_lang_code_keys, metashare.repository.validators.validate_dict_values])),
                ('sex', models.CharField(blank=True, help_text=b'The gender of a person related to or participating in the resource', max_length=30, verbose_name=b'Sex', choices=[('female', 'Female'), ('male', 'Male'), ('unknown', 'Unknown')])),
                ('position', metashare.repository.fields.XmlCharField(help_text=b'The position or the title of a person if affiliated to an organization', max_length=100, verbose_name=b'Position', blank=True)),
                ('source_url', models.URLField(default=b'http://127.0.0.1:8000', help_text=b'(Read-only) base URL for the server where the master copy of the associated entity instance is located.')),
                ('copy_status', models.CharField(default=b'm', help_text=b'Generalized copy status flag for this entity instance.', max_length=1, choices=[(b'm', b'master copy'), (b'r', b'remote copy'), (b'p', b'proxy copy')])),
                ('affiliation', models.ManyToManyField(related_name='affiliation_personinfotype_model_related', to='repository.organizationInfoType_model', blank=True, help_text=b'Groups information on organization to whomtheperson is affiliated', null=True, verbose_name=b'Affiliation')),
                ('communicationInfo', models.OneToOneField(verbose_name=b'Communication', to='repository.communicationInfoType_model', help_text=b'Groups information on communication details of a person or an organization')),
            ],
            options={
                'verbose_name': 'Person',
            },
            bases=('repository.actorinfotype_model',),
        ),
        migrations.CreateModel(
            name='toolServiceInfoType_model',
            fields=[
                ('resourcecomponenttypetype_model_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='repository.resourceComponentTypeType_model')),
                ('resourceType', metashare.repository.fields.XmlCharField(default=b'toolService', help_text=b'The type of the resource that a tool or service takes as input or produces as output', max_length=1000, editable=False, verbose_name=b'Resource')),
                ('toolServiceType', models.CharField(help_text=b'Specifies the type of the tool or service', max_length=100, verbose_name=b'Tool service type', choices=[('architecture', 'Architecture'), ('infrastructure', 'Infrastructure'), ('nlpDevelopmentEnvironment', 'Nlp Development Environment'), ('other', 'Other'), ('platform', 'Platform'), ('service', 'Service'), ('suiteOfTools', 'Suite Of Tools'), ('tool', 'Tool')])),
                ('toolServiceSubtype', metashare.repository.fields.MultiTextField(blank=True, help_text=b'Specifies the subtype of tool or service', max_length=100, verbose_name=b'Tool service subtype', validators=[metashare.repository.validators.validate_matches_xml_char_production])),
                ('languageDependent', metashare.repository.fields.MetaBooleanField(help_text=b'Indicates whether the operation of the tool or service is language dependent or not', verbose_name=b'Language dependent', choices=[(True, b'Yes'), (False, b'No')])),
                ('inputInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.inputInfoType_model', blank=True, help_text=b'Groups together information on the requirements set on the input resource of a tool or service', verbose_name=b'Input')),
                ('outputInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.outputInfoType_model', blank=True, help_text=b'Groups together information on the requirements set on the output of a tool or service', verbose_name=b'Output')),
                ('toolServiceCreationInfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.toolServiceCreationInfoType_model', blank=True, help_text=b'Groups together information on the creation of a tool or service', verbose_name=b'Tool service creation')),
            ],
            options={
                'verbose_name': 'Tool service',
            },
            bases=('repository.resourcecomponenttypetype_model',),
        ),
        migrations.AddField(
            model_name='validationinfotype_model',
            name='validationReport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='repository.documentationInfoType_model', help_text=b'A short account of the validation details or a bibliographic reference to a document with detailed information on the validation process and results', null=True, verbose_name=b'Validation report'),
        ),
        migrations.AddField(
            model_name='validationinfotype_model',
            name='validationTool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='repository.targetResourceInfoType_model', help_text=b'The name, the identifier or the url of the tool used for the validation of the resource', null=True, verbose_name=b'Validation tool'),
        ),
        migrations.AddField(
            model_name='validationinfotype_model',
            name='validator',
            field=models.ManyToManyField(related_name='validator_validationinfotype_model_related', to='repository.actorInfoType_model', blank=True, help_text=b'Groups information on the person(s) or the organization(s) that validated the resource', null=True, verbose_name=b'Validator'),
        ),
        migrations.AddField(
            model_name='toolserviceevaluationinfotype_model',
            name='evaluationReport',
            field=models.ManyToManyField(related_name='evaluationReport_toolserviceevaluationinfotype_model_related', to='repository.documentationInfoType_model', blank=True, help_text=b'A bibliographical record of or link to a report describing the evaluation process, tool, method etc. of the tool or service', null=True, verbose_name=b'Evaluation report'),
        ),
        migrations.AddField(
            model_name='toolserviceevaluationinfotype_model',
            name='evaluationTool',
            field=models.ManyToManyField(related_name='evaluationTool_toolserviceevaluationinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'The name or id or url of the tool used for the evaluation of the tool or service', null=True, verbose_name=b'Evaluation tool'),
        ),
        migrations.AddField(
            model_name='toolserviceevaluationinfotype_model',
            name='evaluator',
            field=models.ManyToManyField(related_name='evaluator_toolserviceevaluationinfotype_model_related', to='repository.actorInfoType_model', blank=True, help_text=b'Groups information on person or organization that evaluated the tool or service', null=True, verbose_name=b'Evaluator'),
        ),
        migrations.AddField(
            model_name='runningenvironmentinfotype_model',
            name='requiredLRs',
            field=models.ManyToManyField(related_name='requiredLRs_runningenvironmentinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'If for running a tool and/or computational grammar, specific LRs (e.g. a grammar, a list of words etc.) are required', null=True, verbose_name=b'Required lrs'),
        ),
        migrations.AddField(
            model_name='runningenvironmentinfotype_model',
            name='requiredSoftware',
            field=models.ManyToManyField(related_name='requiredSoftware_runningenvironmentinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'Additional software required for running a tool and/or computational grammar', null=True, verbose_name=b'Required software'),
        ),
        migrations.AddField(
            model_name='resourceinfotype_model',
            name='resourceComponentType',
            field=models.OneToOneField(verbose_name=b'Resource component', to='repository.resourceComponentTypeType_model', help_text=b'Used for distinguishing between resource types'),
        ),
        migrations.AddField(
            model_name='resourceinfotype_model',
            name='resourceCreationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.resourceCreationInfoType_model', blank=True, help_text=b'Groups information on the creation procedure of a resource', verbose_name=b'Resource creation'),
        ),
        migrations.AddField(
            model_name='resourceinfotype_model',
            name='resourceDocumentationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.resourceDocumentationInfoType_model', blank=True, help_text=b'Groups together information on any document describing the resource', verbose_name=b'Resource documentation'),
        ),
        migrations.AddField(
            model_name='resourceinfotype_model',
            name='storage_object',
            field=models.ForeignKey(null=True, blank=True, to='storage.StorageObject', unique=True),
        ),
        migrations.AddField(
            model_name='resourceinfotype_model',
            name='usageInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.usageInfoType_model', blank=True, help_text=b'Groups information on usage of the resource (both intended and actual use)', verbose_name=b'Usage'),
        ),
        migrations.AddField(
            model_name='resourceinfotype_model',
            name='versionInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.versionInfoType_model', blank=True, help_text=b'Groups information on a specific version or release of the resource', verbose_name=b'Version'),
        ),
        migrations.AddField(
            model_name='resourcedocumentationinfotype_model',
            name='documentation',
            field=models.ManyToManyField(related_name='documentation_resourcedocumentationinfotype_model_related', to='repository.documentationInfoType_model', blank=True, help_text=b'Refers to papers, manuals, reports etc. describing the resource', null=True, verbose_name=b'Documentation'),
        ),
        migrations.AddField(
            model_name='resourcecreationinfotype_model',
            name='resourceCreator',
            field=models.ManyToManyField(related_name='resourceCreator_resourcecreationinfotype_model_related', to='repository.actorInfoType_model', blank=True, help_text=b'Groups information on the person or the organization that has created the resource', null=True, verbose_name=b'Resource creator'),
        ),
        migrations.AddField(
            model_name='relationinfotype_model',
            name='back_to_resourceinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.resourceInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='relationinfotype_model',
            name='relatedResource',
            field=models.ForeignKey(verbose_name=b'Related resource', to='repository.targetResourceInfoType_model', help_text=b'The full name, the identifier or the url of the related resource'),
        ),
        migrations.AddField(
            model_name='recordinginfotype_model',
            name='recorder',
            field=models.ManyToManyField(related_name='recorder_recordinginfotype_model_related', to='repository.actorInfoType_model', blank=True, help_text=b'Information on the recorder(s) of the audio or video part of the resource', null=True, verbose_name=b'Recorder'),
        ),
        migrations.AddField(
            model_name='participantinfotype_model',
            name='back_to_personsourcesetinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.personSourceSetInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='modalityinfotype_model',
            name='sizePerModality',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on the size per modality component', verbose_name=b'Size per modality'),
        ),
        migrations.AddField(
            model_name='licenceinfotype_model',
            name='distributionRightsHolder',
            field=models.ManyToManyField(related_name='distributionRightsHolder_licenceinfotype_model_related', to='repository.actorInfoType_model', blank=True, help_text=b'Groups information on a person or an organization that holds the distribution rights. The range and scope of distribution rights is defined in the distribution agreement. The distributor in most cases only has a limited licence to distribute the work and collect royalties on behalf of the licensor or the IPR holder and cannot give to any recipient of the work permissions that exceed the scope of the distribution agreement (e.g. to allow uses of the work that are not defined in the distribution agreement)', null=True, verbose_name=b'Distribution rights holder'),
        ),
        migrations.AddField(
            model_name='licenceinfotype_model',
            name='licensor',
            field=models.ManyToManyField(related_name='licensor_licenceinfotype_model_related', to='repository.actorInfoType_model', blank=True, help_text=b"Groups information on the person who is legally eligible to licence and actually licenses the resource. The licensor could be different from the creator, the distributor or the IP rightsholder. The licensor has the necessary rights or licences to license the work and is the party that actually licenses the resource that enters the META-SHARE network. She will have obtained the necessary rights or licences from the IPR holder and she may have a distribution agreement with a distributor that disseminates the work under a set of conditions defined in the specific licence and collects revenue on the licensor's behalf. The attribution of the creator, separately from the attribution of the licensor, may be part of the licence under which the resource is distributed (as e.g. is the case with Creative Commons Licences)", null=True, verbose_name=b'Licensor'),
        ),
        migrations.AddField(
            model_name='licenceinfotype_model',
            name='membershipInfo',
            field=models.ManyToManyField(related_name='membershipInfo_licenceinfotype_model_related', to='repository.membershipInfoType_model', blank=True, help_text=b'The conditions imposed by the user being member of some association/institution (e.g., ELRA, LDC) distributing the resource. This indicates the availability conditions (and prices) for users who are members or not', null=True, verbose_name=b'Membership'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourcevideoinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lingualityInfoType_model', blank=True, help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other', verbose_name=b'Linguality'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourcevideoinfotype_model',
            name='videoContentInfo',
            field=models.OneToOneField(verbose_name=b'Video content', to='repository.videoContentInfoType_model', help_text=b'Groups together information on the contents of the video part of a resource'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourcetextinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(verbose_name=b'Linguality', to='repository.lingualityInfoType_model', help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourcemediatypetype_model',
            name='lexicalConceptualResourceTextInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lexicalConceptualResourceTextInfoType_model', blank=True, help_text=b'Groups information on the textual part of the lexical/conceptual resource', verbose_name=b'Lexical conceptual resource text'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourcemediatypetype_model',
            name='lexicalConceptualResourceVideoInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lexicalConceptualResourceVideoInfoType_model', blank=True, help_text=b'Groups information on the video part of the lexical conceptual resource', verbose_name=b'Lexical conceptual resource video'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourceimageinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lingualityInfoType_model', blank=True, help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other', verbose_name=b'Linguality'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourceaudioinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lingualityInfoType_model', blank=True, help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other', verbose_name=b'Linguality'),
        ),
        migrations.AddField(
            model_name='languagevarietyinfotype_model',
            name='sizePerLanguageVariety',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on the size per language variety component', verbose_name=b'Size per language variety'),
        ),
        migrations.AddField(
            model_name='languageinfotype_model',
            name='back_to_lexicalconceptualresourceaudioinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceAudioInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='languageinfotype_model',
            name='back_to_lexicalconceptualresourceimageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceImageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='languageinfotype_model',
            name='back_to_lexicalconceptualresourcetextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='languageinfotype_model',
            name='back_to_lexicalconceptualresourcevideoinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceVideoInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='languageinfotype_model',
            name='languageVarietyInfo',
            field=models.ManyToManyField(related_name='languageVarietyInfo_languageinfotype_model_related', to='repository.languageVarietyInfoType_model', blank=True, help_text=b'Groups information on language varieties occurred in the resource (e.g. dialects)', null=True, verbose_name=b'Language variety'),
        ),
        migrations.AddField(
            model_name='languageinfotype_model',
            name='sizePerLanguage',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on the size per language component', verbose_name=b'Size per language'),
        ),
        migrations.AddField(
            model_name='languagedescriptionvideoinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lingualityInfoType_model', blank=True, help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other', verbose_name=b'Linguality'),
        ),
        migrations.AddField(
            model_name='languagedescriptionvideoinfotype_model',
            name='videoContentInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.videoContentInfoType_model', blank=True, help_text=b'Groups together information on the contents of the video part of a resource', verbose_name=b'Video content'),
        ),
        migrations.AddField(
            model_name='languagedescriptiontextinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(verbose_name=b'Linguality', to='repository.lingualityInfoType_model', help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other'),
        ),
        migrations.AddField(
            model_name='languagedescriptiontextinfotype_model',
            name='modalityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.modalityInfoType_model', blank=True, help_text=b'Groups information on the modalities represented in the resource', verbose_name=b'Modality'),
        ),
        migrations.AddField(
            model_name='languagedescriptionoperationinfotype_model',
            name='relatedLexiconInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.relatedLexiconInfoType_model', blank=True, help_text=b'Groups together information on requirements for lexica set by the LanguageDescriptions', verbose_name=b'Related lexicon'),
        ),
        migrations.AddField(
            model_name='languagedescriptionoperationinfotype_model',
            name='runningEnvironmentInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.runningEnvironmentInfoType_model', blank=True, help_text=b'Groups together information on the running environment of a tool or a language description', verbose_name=b'Running environment'),
        ),
        migrations.AddField(
            model_name='languagedescriptionmediatypetype_model',
            name='languageDescriptionTextInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.languageDescriptionTextInfoType_model', blank=True, help_text=b'Groups together all information relevant to the text module of a language description (e.g. format, languages, size etc.); it is obligatory for all language descriptions', verbose_name=b'Language description text'),
        ),
        migrations.AddField(
            model_name='languagedescriptionmediatypetype_model',
            name='languageDescriptionVideoInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.languageDescriptionVideoInfoType_model', blank=True, help_text=b'Groups together all information relevant to the video parts of a language description (e.g. format, languages, size etc.), if there are any (e.g. for sign language grammars)', verbose_name=b'Language description video'),
        ),
        migrations.AddField(
            model_name='languagedescriptionimageinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lingualityInfoType_model', blank=True, help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other', verbose_name=b'Linguality'),
        ),
        migrations.AddField(
            model_name='imageformatinfotype_model',
            name='back_to_languagedescriptionimageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.languageDescriptionImageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='imageformatinfotype_model',
            name='back_to_lexicalconceptualresourceimageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceImageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='imageformatinfotype_model',
            name='compressionInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.compressionInfoType_model', blank=True, help_text=b'Groups together information on the compression status and method of a resource', verbose_name=b'Compression'),
        ),
        migrations.AddField(
            model_name='imageformatinfotype_model',
            name='resolutionInfo',
            field=models.ManyToManyField(related_name='resolutionInfo_imageformatinfotype_model_related', to='repository.resolutionInfoType_model', blank=True, help_text=b'Groups together information on the image resolution', null=True, verbose_name=b'Resolution'),
        ),
        migrations.AddField(
            model_name='imageformatinfotype_model',
            name='sizePerImageFormat',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Used to give info on size of parts of a resource that differ as to the format', verbose_name=b'Size per image format'),
        ),
        migrations.AddField(
            model_name='imagecontentinfotype_model',
            name='staticElementInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.staticElementInfoType_model', blank=True, help_text=b'Groups information on the static element visible on the images', verbose_name=b'Static element'),
        ),
        migrations.AddField(
            model_name='imageclassificationinfotype_model',
            name='sizePerImageClassification',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on size of parts with different image classification', verbose_name=b'Size per image classification'),
        ),
        migrations.AddField(
            model_name='geographiccoverageinfotype_model',
            name='back_to_languagedescriptionimageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.languageDescriptionImageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='geographiccoverageinfotype_model',
            name='back_to_languagedescriptiontextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.languageDescriptionTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='geographiccoverageinfotype_model',
            name='back_to_languagedescriptionvideoinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.languageDescriptionVideoInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='geographiccoverageinfotype_model',
            name='back_to_lexicalconceptualresourceaudioinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceAudioInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='geographiccoverageinfotype_model',
            name='back_to_lexicalconceptualresourceimageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceImageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='geographiccoverageinfotype_model',
            name='back_to_lexicalconceptualresourcetextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='geographiccoverageinfotype_model',
            name='back_to_lexicalconceptualresourcevideoinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceVideoInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='geographiccoverageinfotype_model',
            name='sizePerGeographicCoverage',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on size per geographically distinct section of the resource', verbose_name=b'Size per geographic coverage'),
        ),
        migrations.AddField(
            model_name='foreseenuseinfotype_model',
            name='back_to_usageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.usageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='domaininfotype_model',
            name='back_to_languagedescriptionimageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.languageDescriptionImageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='domaininfotype_model',
            name='back_to_languagedescriptiontextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.languageDescriptionTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='domaininfotype_model',
            name='back_to_languagedescriptionvideoinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.languageDescriptionVideoInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='domaininfotype_model',
            name='back_to_lexicalconceptualresourceaudioinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceAudioInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='domaininfotype_model',
            name='back_to_lexicalconceptualresourceimageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceImageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='domaininfotype_model',
            name='back_to_lexicalconceptualresourcetextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='domaininfotype_model',
            name='back_to_lexicalconceptualresourcevideoinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceVideoInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='domaininfotype_model',
            name='sizePerDomain',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Specifies the size of resource parts per domain', verbose_name=b'Size per domain'),
        ),
        migrations.AddField(
            model_name='distributioninfotype_model',
            name='iprHolder',
            field=models.ManyToManyField(related_name='iprHolder_distributioninfotype_model_related', to='repository.actorInfoType_model', blank=True, help_text=b'Groups information on a person or an organization who holds the full Intellectual Property Rights (Copyright, trademark etc) that subsist in the resource. The IPR holder could be different from the creator that may have assigned the rights to the IPR holder (e.g. an author as a creator assigns her rights to the publisher who is the IPR holder) and the distributor that holds a specific licence (i.e. a permission) to distribute the work within the META-SHARE network.', null=True, verbose_name=b'Ipr holder'),
        ),
        migrations.AddField(
            model_name='creationinfotype_model',
            name='creationTool',
            field=models.ManyToManyField(related_name='creationTool_creationinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'The name, the identifier or the url of the tool used in the creation process', null=True, verbose_name=b'Creation tool'),
        ),
        migrations.AddField(
            model_name='creationinfotype_model',
            name='originalSource',
            field=models.ManyToManyField(related_name='originalSource_creationinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'The name, the identifier or the url of thethe original resources that were at the base of the creation process of the resource', null=True, verbose_name=b'Original source'),
        ),
        migrations.AddField(
            model_name='corpusvideoinfotype_model',
            name='creationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation'),
        ),
        migrations.AddField(
            model_name='corpusvideoinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lingualityInfoType_model', blank=True, help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other', verbose_name=b'Linguality'),
        ),
        migrations.AddField(
            model_name='corpusvideoinfotype_model',
            name='modalityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.modalityInfoType_model', blank=True, help_text=b'Groups information on the modalities represented in the resource', verbose_name=b'Modality'),
        ),
        migrations.AddField(
            model_name='corpusvideoinfotype_model',
            name='recordingInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.recordingInfoType_model', blank=True, help_text=b'Groups together information on the recording of the audio or video part of a resource', verbose_name=b'Recording'),
        ),
        migrations.AddField(
            model_name='corpusvideoinfotype_model',
            name='settingInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.settingInfoType_model', blank=True, help_text=b'Groups together information on the setting of the audio and/or video part of a resource', verbose_name=b'Setting'),
        ),
        migrations.AddField(
            model_name='corpusvideoinfotype_model',
            name='videoContentInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.videoContentInfoType_model', blank=True, help_text=b'Groups together information on the contents of the video part of a resource', verbose_name=b'Video content'),
        ),
        migrations.AddField(
            model_name='corpustextnumericalinfotype_model',
            name='creationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation'),
        ),
        migrations.AddField(
            model_name='corpustextnumericalinfotype_model',
            name='recordingInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.recordingInfoType_model', blank=True, help_text=b'Groups together information on the recording of the audio or video part of a resource', verbose_name=b'Recording'),
        ),
        migrations.AddField(
            model_name='corpustextnumericalinfotype_model',
            name='textNumericalContentInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.textNumericalContentInfoType_model', blank=True, help_text=b'Groups information on the content of the textNumerical part of the resource', verbose_name=b'Text numerical content'),
        ),
        migrations.AddField(
            model_name='corpustextngraminfotype_model',
            name='creationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation'),
        ),
        migrations.AddField(
            model_name='corpustextngraminfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(verbose_name=b'Linguality', to='repository.lingualityInfoType_model', help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other'),
        ),
        migrations.AddField(
            model_name='corpustextngraminfotype_model',
            name='modalityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.modalityInfoType_model', blank=True, help_text=b'Groups information on the modalities represented in the resource', verbose_name=b'Modality'),
        ),
        migrations.AddField(
            model_name='corpustextngraminfotype_model',
            name='ngramInfo',
            field=models.OneToOneField(verbose_name=b'Ngram', to='repository.ngramInfoType_model'),
        ),
        migrations.AddField(
            model_name='corpustextinfotype_model',
            name='creationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation'),
        ),
        migrations.AddField(
            model_name='corpustextinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(verbose_name=b'Linguality', to='repository.lingualityInfoType_model', help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other'),
        ),
        migrations.AddField(
            model_name='corpusmediatypetype_model',
            name='corpusTextNgramInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.corpusTextNgramInfoType_model', blank=True, help_text=b'Groups together information required for n-gram resources; information can be provided both as regards features drawn from the source corpus (e.g. language coverage, size, format, domains etc.) and features pertaining to the n-gram output itself (e.g. range of n-grams, type of item included, etc.)', verbose_name=b'Corpus text ngram'),
        ),
        migrations.AddField(
            model_name='corpusmediatypetype_model',
            name='corpusTextNumericalInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.corpusTextNumericalInfoType_model', blank=True, help_text=b'Groups together information on the textNumerical component of a corpus. It is used basically for the textual representation of measurements and observations linked to sensorimotor recordings', verbose_name=b'Corpus text numerical'),
        ),
        migrations.AddField(
            model_name='corpusimageinfotype_model',
            name='creationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation'),
        ),
        migrations.AddField(
            model_name='corpusimageinfotype_model',
            name='imageContentInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.imageContentInfoType_model', blank=True, help_text=b'Groups together information on the contents of the image part of a resource', verbose_name=b'Image content'),
        ),
        migrations.AddField(
            model_name='corpusimageinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lingualityInfoType_model', blank=True, help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other', verbose_name=b'Linguality'),
        ),
        migrations.AddField(
            model_name='corpusaudioinfotype_model',
            name='creationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation'),
        ),
        migrations.AddField(
            model_name='corpusaudioinfotype_model',
            name='lingualityInfo',
            field=models.OneToOneField(verbose_name=b'Linguality', to='repository.lingualityInfoType_model', help_text=b'Groups information on the number of languages of the resource part and of the way they are combined to each other'),
        ),
        migrations.AddField(
            model_name='corpusaudioinfotype_model',
            name='recordingInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.recordingInfoType_model', blank=True, help_text=b'Groups together information on the recording of the audio or video part of a resource', verbose_name=b'Recording'),
        ),
        migrations.AddField(
            model_name='corpusaudioinfotype_model',
            name='settingInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.settingInfoType_model', blank=True, help_text=b'Groups together information on the setting of the audio and/or video part of a resource', verbose_name=b'Setting'),
        ),
        migrations.AddField(
            model_name='characterencodinginfotype_model',
            name='back_to_corpustextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='characterencodinginfotype_model',
            name='back_to_corpustextngraminfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='characterencodinginfotype_model',
            name='back_to_languagedescriptiontextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.languageDescriptionTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='characterencodinginfotype_model',
            name='back_to_lexicalconceptualresourcetextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='characterencodinginfotype_model',
            name='sizePerCharacterEncoding',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on the size of the resource parts with different character encoding', verbose_name=b'Size per character encoding'),
        ),
        migrations.AddField(
            model_name='captureinfotype_model',
            name='personSourceSetInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.personSourceSetInfoType_model', blank=True, help_text=b'Groups information on the persons (speakers, video participants, etc.) in the audio andvideoparts of the resource', verbose_name=b'Person source set'),
        ),
        migrations.AddField(
            model_name='audioformatinfotype_model',
            name='back_to_corpusaudioinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='audioformatinfotype_model',
            name='back_to_lexicalconceptualresourceaudioinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.lexicalConceptualResourceAudioInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='audioformatinfotype_model',
            name='compressionInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.compressionInfoType_model', blank=True, help_text=b'Groups together information on the compression status and method of a resource', verbose_name=b'Compression'),
        ),
        migrations.AddField(
            model_name='audioformatinfotype_model',
            name='sizePerAudioFormat',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Used to give info on size of parts of a resource that differ as to the format', verbose_name=b'Size per audio format'),
        ),
        migrations.AddField(
            model_name='audioclassificationinfotype_model',
            name='back_to_corpusaudioinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='audioclassificationinfotype_model',
            name='sizePerAudioClassification',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'The size of the audio subparts of the resource in terms of classification criteria', verbose_name=b'Size per audio classification'),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='annotationManual',
            field=models.ManyToManyField(related_name='annotationManual_annotationinfotype_model_related', to='repository.documentationInfoType_model', blank=True, help_text=b'A bibliographic reference or ms:httpURI link to the annotation manual', null=True, verbose_name=b'Annotation manual'),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='annotationTool',
            field=models.ManyToManyField(related_name='annotationTool_annotationinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'The name, the identifier or the url of the tool used for the annotation of the resource', null=True, verbose_name=b'Annotation tool'),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='annotator',
            field=models.ManyToManyField(related_name='annotator_annotationinfotype_model_related', to='repository.actorInfoType_model', blank=True, help_text=b'Groups information on the annotators of the specific annotation type', null=True, verbose_name=b'Annotator'),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='back_to_corpusaudioinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusAudioInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='back_to_corpusimageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusImageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='back_to_corpustextinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusTextInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='back_to_corpustextngraminfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusTextNgramInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='back_to_corpustextnumericalinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusTextNumericalInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='back_to_corpusvideoinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.corpusVideoInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='annotationinfotype_model',
            name='sizePerAnnotation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.sizeInfoType_model', blank=True, help_text=b'Provides information on size for the annotated parts of the resource', verbose_name=b'Size per annotation'),
        ),
        migrations.AddField(
            model_name='actualuseinfotype_model',
            name='back_to_usageinfotype_model',
            field=models.ForeignKey(blank=True, to='repository.usageInfoType_model', null=True),
        ),
        migrations.AddField(
            model_name='actualuseinfotype_model',
            name='derivedResource',
            field=models.ManyToManyField(related_name='derivedResource_actualuseinfotype_model_related', to='repository.targetResourceInfoType_model', blank=True, help_text=b'The name, the identifier or the url of the outcome or product of the resource.', null=True, verbose_name=b'Derived resource'),
        ),
        migrations.AddField(
            model_name='actualuseinfotype_model',
            name='usageProject',
            field=models.ManyToManyField(related_name='usageProject_actualuseinfotype_model_related', to='repository.projectInfoType_model', blank=True, help_text=b'Groups information on the project in which the resource has been used', null=True, verbose_name=b'Usage project'),
        ),
        migrations.AddField(
            model_name='actualuseinfotype_model',
            name='usageReport',
            field=models.ManyToManyField(related_name='usageReport_actualuseinfotype_model_related', to='repository.documentationInfoType_model', blank=True, help_text=b'Reports on the research papers documenting the usage of a resource, either in a structured form or in free text', null=True, verbose_name=b'Usage report'),
        ),
        migrations.AddField(
            model_name='toolserviceinfotype_model',
            name='toolServiceEvaluationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.toolServiceEvaluationInfoType_model', blank=True, help_text=b'Groups together information on the evaluation status of a tool or service', verbose_name=b'Tool service evaluation'),
        ),
        migrations.AddField(
            model_name='toolserviceinfotype_model',
            name='toolServiceOperationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.toolServiceOperationInfoType_model', blank=True, help_text=b'Groups together information on the operation of a tool or service', verbose_name=b'Tool service operation'),
        ),
        migrations.AddField(
            model_name='resourceinfotype_model',
            name='contactPerson',
            field=models.ManyToManyField(help_text=b'Groups information on the person(s) that is/are responsible for providing further information regarding the resource', related_name='contactPerson_resourceinfotype_model_related', verbose_name=b'Contact person', to='repository.personInfoType_model'),
        ),
        migrations.AddField(
            model_name='personlisttype_model',
            name='personInfo',
            field=models.ManyToManyField(related_name='personInfo_personlisttype_model_related', verbose_name=b'Person', to='repository.personInfoType_model'),
        ),
        migrations.AddField(
            model_name='organizationlisttype_model',
            name='organizationInfo',
            field=models.ManyToManyField(related_name='organizationInfo_organizationlisttype_model_related', verbose_name=b'Organization', to='repository.organizationInfoType_model'),
        ),
        migrations.AddField(
            model_name='metadatainfotype_model',
            name='metadataCreator',
            field=models.ManyToManyField(related_name='metadataCreator_metadatainfotype_model_related', to='repository.personInfoType_model', blank=True, help_text=b'Groups information on the person that has created the metadata record', null=True, verbose_name=b'Metadata creator'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourceinfotype_model',
            name='creationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourceinfotype_model',
            name='lexicalConceptualResourceEncodingInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.lexicalConceptualResourceEncodingInfoType_model', blank=True, help_text=b'Groups all information regarding the contents of lexical/conceptual resources', verbose_name=b'Lexical conceptual resource encoding'),
        ),
        migrations.AddField(
            model_name='lexicalconceptualresourceinfotype_model',
            name='lexicalConceptualResourceMediaType',
            field=models.OneToOneField(verbose_name=b'Lexical conceptual resource media', to='repository.lexicalConceptualResourceMediaTypeType_model', help_text=b'Restriction of mediaType for lexicalConceptualResources'),
        ),
        migrations.AddField(
            model_name='languagedescriptioninfotype_model',
            name='creationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.creationInfoType_model', blank=True, help_text=b'Groups together information on the resource creation (e.g. for corpora, selection of texts/audio files/ video files etc. and structural encoding thereof; for lexica, construction of lemma list etc.)', verbose_name=b'Creation'),
        ),
        migrations.AddField(
            model_name='languagedescriptioninfotype_model',
            name='languageDescriptionEncodingInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.languageDescriptionEncodingInfoType_model', blank=True, help_text=b'Groups together information on the contents of the LanguageDescriptions', verbose_name=b'Language description encoding'),
        ),
        migrations.AddField(
            model_name='languagedescriptioninfotype_model',
            name='languageDescriptionMediaType',
            field=models.OneToOneField(verbose_name=b'Language description media', to='repository.languageDescriptionMediaTypeType_model', help_text=b'Groups information on the media type-specific components for language descriptions'),
        ),
        migrations.AddField(
            model_name='languagedescriptioninfotype_model',
            name='languageDescriptionOperationInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.languageDescriptionOperationInfoType_model', blank=True, help_text=b'Groups together information on the operation requirements of the Language Descriptions', verbose_name=b'Language description operation'),
        ),
        migrations.AddField(
            model_name='languagedescriptioninfotype_model',
            name='languageDescriptionPerformanceInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.languageDescriptionPerformanceInfoType_model', blank=True, help_text=b'Groups together information on the performance of the Language Descriptions', verbose_name=b'Language description performance'),
        ),
        migrations.AddField(
            model_name='documentlisttype_model',
            name='documentInfo',
            field=models.ManyToManyField(related_name='documentInfo_documentlisttype_model_related', verbose_name=b'Document', to='repository.documentInfoType_model'),
        ),
        migrations.AddField(
            model_name='corpusinfotype_model',
            name='corpusMediaType',
            field=models.OneToOneField(verbose_name=b'Corpus media', to='repository.corpusMediaTypeType_model', help_text=b'Used to specify the media type specific to corpora and group together the relevant information'),
        ),
    ]
