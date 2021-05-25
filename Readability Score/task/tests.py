from typing import List, Any
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TestClue:

    def __init__(self, words, diffs, sentences, characters, syllables, polysyllables,
                 ari, fkri, smog, cli, prob_score, age):
        self.words = words
        self.diffs = diffs
        self.sentences = sentences
        self.characters = characters
        self.syllables = syllables
        self.polysyllables = polysyllables
        self.ari = ari
        self.fkri = fkri
        self.smog = smog
        self.cli = cli
        self.prob_score = prob_score
        self.age = age


class TestTheFifth(StageTest):
    file_words = "words.txt"
    words = " ".join(
        ['carrot', 'dude', 'mind', 'some', 'wander', 'a', 'abandon', 'ability', 'able', 'about', 'above', 'abroad',
         'absence', 'absolute', 'absolutely', 'absorb', 'abuse', 'academic', 'accept', 'acceptable', 'access',
         'accident', 'accommodation', 'accompany', 'according', 'account', 'accurate', 'accuse', 'achieve',
         'achievement', 'acid', 'acknowledge', 'acquire', 'across', 'act', 'action', 'active', 'activist', 'activity',
         'actor', 'actual', 'actually', 'ad', 'adapt', 'add', 'addition', 'additional', 'address', 'adequate', 'adjust',
         'administration', 'administrative', 'admire', 'admission', 'admit', 'adopt', 'adult', 'advance', 'advanced',
         'advantage', 'advert', 'advertise', 'advertisement', 'advertising', 'advice', 'advise', 'adviser', 'affair',
         'affect', 'afford', 'afraid', 'after', 'afternoon', 'afterwards', 'again', 'against', 'age', 'aged', 'agency',
         'agent', 'aggressive', 'ago', 'agree', 'agreement', 'agriculture', 'ahead', 'aid', 'aim', 'air', 'aircraft',
         'airline', 'airport', 'alarm', 'album', 'alcohol', 'alive', 'all', 'allow', 'allowance', 'almost', 'alone',
         'along', 'alongside', 'already', 'also', 'alter', 'alternative', 'although', 'altogether', 'always', 'amazing',
         'ambition', 'ambulance', 'among', 'amount', 'an', 'analyse', 'analysis', 'analyst', 'ancient', 'and', 'anger',
         'angle', 'angry', 'animal', 'announce', 'announcement', 'annoy', 'annual', 'another', 'answer', 'anticipate',
         'anxiety', 'anxious', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'apart',
         'apartment', 'apologize', 'apology', 'apparent', 'apparently', 'appeal', 'appear', 'appearance', 'apple',
         'application', 'apply', 'appoint', 'appointment', 'appreciate', 'approach', 'appropriate', 'approval',
         'approve', 'approximate', 'architect', 'architecture', 'area', 'argue', 'argument', 'arise', 'arm', 'armed',
         'army', 'around', 'arrange', 'arrangement', 'arrest', 'arrival', 'arrive', 'art', 'article', 'artificial',
         'artist', 'as', 'ashamed', 'aside', 'ask', 'asleep', 'aspect', 'assess', 'assessment', 'assignment', 'assist',
         'assistance', 'assistant', 'associate', 'association', 'assume', 'assumption', 'assure', 'at', 'atmosphere',
         'attach', 'attack', 'attempt', 'attend', 'attention', 'attitude', 'attorney', 'attract', 'attraction',
         'attractive', 'audience', 'aunt', 'author', 'authority', 'automatic', 'automatically', 'autumn', 'available',
         'average', 'avoid', 'awake', 'award', 'aware', 'awareness', 'away', 'awful', 'awkward', 'baby', 'back',
         'background', 'backwards', 'bacon', 'bad', 'badly', 'bag', 'bake', 'balance', 'ball', 'ban', 'band', 'bang',
         'bank', 'bar', 'barrier', 'base', 'baseball', 'basic', 'basically', 'basis', 'basket', 'bat', 'bath',
         'bathroom', 'battery', 'battle', 'be', 'beach', 'bean', 'bear', 'beard', 'beat', 'beautiful', 'beauty',
         'because', 'become', 'bed', 'bedroom', 'beef', 'beer', 'before', 'beforehand', 'begin', 'beginning', 'behalf',
         'behave', 'behaviour', 'behind', 'being', 'belief', 'believe', 'bell', 'belong', 'below', 'belt', 'bench',
         'bend', 'beneath', 'benefit', 'beside', 'best', 'bet', 'better', 'between', 'beyond', 'bicycle', 'bid', 'big',
         'bike', 'bill', 'bin', 'bird', 'birth', 'birthday', 'biscuit', 'bit', 'bite', 'bitter', 'black', 'blade',
         'blame', 'blank', 'bless', 'blind', 'block', 'bloke', 'blonde', 'blood', 'blow', 'blue', 'board', 'boat',
         'body', 'boil', 'boiler', 'boiling', 'bomb', 'bone', 'bonus', 'book', 'boom', 'boot', 'border', 'bored',
         'boring', 'born', 'borrow', 'boss', 'both', 'bother', 'bottle', 'bottom', 'bounce', 'bound', 'bowl', 'box',
         'boy', 'boyfriend', 'brain', 'branch', 'brave', 'bread', 'break', 'breakfast', 'breast', 'breath', 'breathe',
         'brick', 'bridge', 'brief', 'briefly', 'bright', 'brilliant', 'bring', 'broad', 'brother', 'brown', 'brush',
         'buck', 'bucket', 'buddy', 'budget', 'bug', 'build', 'builder', 'building', 'bump', 'bunch', 'burn', 'burst',
         'bury', 'bus', 'business', 'busy', 'but', 'butcher', 'butter', 'button', 'buy', 'buyer', 'by', 'bye',
         'cabinet', 'cable', 'cake', 'calculate', 'calculation', 'calculator', 'calendar', 'call', 'calm', 'camera',
         'camp', 'campaign', 'can', 'cancel', 'cancer', 'candidate', 'candle', 'candy', 'cap', 'capable', 'capacity',
         'capital', 'captain', 'capture', 'car', 'card', 'care', 'career', 'careful', 'carefully', 'carpet', 'carry',
         'cartoon', 'case', 'cash', 'cast', 'castle', 'cat', 'catalogue', 'catch', 'category', 'cause', 'cease',
         'ceiling', 'celebrate', 'celebration', 'cell', 'cellphone', 'cent', 'centimetre', 'central', 'centre',
         'century', 'cereal', 'certain', 'certainly', 'certificate', 'chain', 'chair', 'chairman', 'challenge',
         'champion', 'championship', 'chance', 'change', 'channel', 'chap', 'chapter', 'character', 'characteristic',
         'characterize', 'charge', 'charity', 'chart', 'chase', 'chat', 'cheap', 'cheat', 'check', 'cheek', 'cheese',
         'chemical', 'chemist', 'chemistry', 'cheque', 'cherry', 'chest', 'chicken', 'chief', 'child', 'childhood',
         'chip', 'chocolate', 'choice', 'choose', 'chop', 'chuck', 'church', 'cigarette', 'cinema', 'circle', 'circuit',
         'circumstance', 'citizen', 'city', 'civil', 'claim', 'class', 'classic', 'classical', 'classroom', 'clean',
         'cleaner', 'clear', 'clearly', 'clerk', 'clever', 'click', 'client', 'climate', 'climb', 'clock', 'close',
         'closed', 'closely', 'closet', 'cloth', 'clothes', 'cloud', 'club', 'clue', 'coach', 'coal', 'coast', 'coat',
         'code', 'coffee', 'coin', 'cold', 'collapse', 'collar', 'colleague', 'collect', 'collection', 'college',
         'colour', 'column', 'combination', 'combine', 'come', 'comfort', 'comfortable', 'command', 'comment',
         'commercial', 'commission', 'commit', 'commitment', 'committee', 'common', 'communicate', 'communication',
         'community', 'company', 'compare', 'comparison', 'compete', 'competition', 'competitive', 'complain',
         'complaint', 'complete', 'completely', 'complex', 'complicated', 'component', 'comprehensive', 'comprise',
         'computer', 'concentrate', 'concentration', 'concept', 'concern', 'concerned', 'concerning', 'concert',
         'conclude', 'conclusion', 'condition', 'conduct', 'conference', 'confidence', 'confident', 'confine',
         'confirm', 'conflict', 'confused', 'confusing', 'confusion', 'congratulation', 'connect', 'connection',
         'conscious', 'consciousness', 'consent', 'consequence', 'consider', 'considerable', 'considerably',
         'consideration', 'consist', 'consistent', 'constant', 'constantly', 'constitute', 'construct', 'construction',
         'consult', 'consumer', 'consumption', 'contact', 'contain', 'contemporary', 'content', 'contest', 'context',
         'continue', 'continuous', 'contract', 'contrast', 'contribute', 'contribution', 'control', 'convenient',
         'convention', 'conventional', 'conversation', 'convert', 'conviction', 'convince', 'cook', 'cooker', 'cookie',
         'cool', 'cooperation', 'cope', 'copy', 'core', 'corn', 'corner', 'correct', 'corridor', 'cost', 'cottage',
         'cotton', 'could', 'council', 'count', 'counter', 'country', 'countryside', 'county', 'couple', 'courage',
         'course', 'court', 'cousin', 'cover', 'cow', 'crack', 'craft', 'crash', 'crazy', 'create', 'creation',
         'creative', 'creature', 'credit', 'crew', 'crime', 'criminal', 'crisis', 'criterion', 'critic', 'critical',
         'criticism', 'criticize', 'crop', 'cross', 'crowd', 'crown', 'crucial', 'cruel', 'cry', 'cultural', 'culture',
         'cup', 'cupboard', 'curious', 'currency', 'current', 'currently', 'curtain', 'curve', 'cushion', 'custom',
         'customer', 'cut', 'cute', 'cycle', 'dad', 'daddy', 'daft', 'daily', 'damage', 'dance', 'danger', 'dangerous',
         'dare', 'dark', 'darkness', 'darling', 'data', 'database', 'date', 'daughter', 'day', 'dead', 'deaf', 'deal',
         'dealer', 'dear', 'death', 'debate', 'debt', 'decade', 'decent', 'decide', 'decision', 'declare', 'decline',
         'deep', 'deeply', 'defeat', 'defence', 'defend', 'define', 'definite', 'definitely', 'definition', 'degree',
         'delay', 'deliberately', 'deliver', 'delivery', 'demand', 'democracy', 'democratic', 'demonstrate',
         'demonstration', 'dentist', 'deny', 'department', 'departure', 'depend', 'dependent', 'deposit', 'depression',
         'depth', 'derive', 'describe', 'description', 'desert', 'deserve', 'design', 'designer', 'desire', 'desk',
         'desperate', 'despite', 'destroy', 'destruction', 'detail', 'detailed', 'detect', 'determination', 'determine',
         'determined', 'develop', 'development', 'device', 'devil', 'diagram', 'diamond', 'diary', 'die', 'diet',
         'differ', 'difference', 'different', 'difficult', 'difficulty', 'dig', 'dimension', 'dinner', 'direct',
         'direction', 'directly', 'director', 'directory', 'dirt', 'dirty', 'disabled', 'disagree', 'disappear',
         'disappoint', 'disappointed', 'disaster', 'disc', 'discipline', 'discount', 'discover', 'discovery', 'discuss',
         'discussion', 'disease', 'disgusting', 'dish', 'disk', 'dismiss', 'display', 'dispute', 'distance', 'distant',
         'distinct', 'distinction', 'distinguish', 'distribute', 'distribution', 'district', 'disturb', 'divide',
         'division', 'divorce', 'do', 'doctor', 'document', 'dog', 'dollar', 'domestic', 'dominant', 'dominate', 'door',
         'dot', 'double', 'doubt', 'down', 'downstairs', 'downtown', 'dozen', 'draft', 'drag', 'drama', 'dramatic',
         'draw', 'drawer', 'drawing', 'dream', 'dress', 'drink', 'drive', 'driver', 'drop', 'drug', 'drunk', 'dry',
         'duck', 'due', 'dull', 'dumb', 'dump', 'during', 'dust', 'duty', 'each', 'ear', 'early', 'earn', 'earth',
         'ease', 'easily', 'east', 'eastern', 'easy', 'eat', 'economic', 'economics', 'economy', 'edge', 'edition',
         'editor', 'education', 'educational', 'effect', 'effective', 'effectively', 'efficiency', 'efficient',
         'effort', 'egg', 'either', 'elderly', 'elect', 'election', 'electric', 'electrical', 'electricity',
         'electronic', 'element', 'elevator', 'else', 'elsewhere', 'email', 'embarrassed', 'emerge', 'emergency',
         'emotion', 'emotional', 'emphasis', 'emphasize', 'empire', 'employ', 'employee', 'employer', 'employment',
         'empty', 'enable', 'encounter', 'encourage', 'encouraging', 'end', 'enemy', 'energy', 'engage', 'engine',
         'engineer', 'engineering', 'enhance', 'enjoy', 'enjoyable', 'enormous', 'enough', 'enquiry', 'ensure', 'enter',
         'enterprise', 'entertainment', 'enthusiasm', 'enthusiastic', 'entire', 'entirely', 'entitle', 'entrance',
         'entry', 'envelope', 'environment', 'environmental', 'equal', 'equally', 'equipment', 'equivalent', 'era',
         'error', 'escape', 'especially', 'essay', 'essential', 'essentially', 'establish', 'establishment', 'estate',
         'estimate', 'ethnic', 'even', 'evening', 'event', 'eventually', 'ever', 'every', 'everybody', 'everyone',
         'everything', 'everywhere', 'evidence', 'evil', 'exact', 'exactly', 'exam', 'examination', 'examine',
         'example', 'excellent', 'except', 'exception', 'exchange', 'excitement', 'exciting', 'exclude', 'excuse',
         'executive', 'exercise', 'exhibition', 'exist', 'existence', 'existing', 'exit', 'expand', 'expansion',
         'expect', 'expectation', 'expenditure', 'expense', 'expensive', 'experience', 'experienced', 'experiment',
         'experimental', 'expert', 'explain', 'explanation', 'explore', 'explosion', 'export', 'expose', 'express',
         'expression', 'extend', 'extension', 'extensive', 'extent', 'external', 'extra', 'extraordinary', 'extreme',
         'extremely', 'eye', 'face', 'facility', 'fact', 'factor', 'factory', 'fail', 'failure', 'fair', 'fairly',
         'faith', 'fall', 'false', 'familiar', 'family', 'famous', 'fan', 'fancy', 'fantastic', 'far', 'farm', 'farmer',
         'fascinating', 'fashion', 'fast', 'fat', 'father', 'fault', 'favour', 'favourite', 'fear', 'feature',
         'federal', 'fee', 'feed', 'feedback', 'feel', 'feeling', 'fellow', 'female', 'fence', 'festival', 'fetch',
         'few', 'field', 'fight', 'figure', 'file', 'fill', 'film', 'filthy', 'final', 'finally', 'finance',
         'financial', 'find', 'finding', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'firstly', 'fish',
         'fishing', 'fit', 'fix', 'fixed', 'flash', 'flat', 'flavour', 'flesh', 'flight', 'flood', 'floor', 'flow',
         'flower', 'fly', 'focus', 'fold', 'folk', 'follow', 'following', 'food', 'foot', 'football', 'for', 'force',
         'foreign', 'forest', 'forever', 'forget', 'forgive', 'fork', 'form', 'formal', 'formally', 'formation',
         'former', 'formula', 'forth', 'fortnight', 'fortunate', 'fortune', 'forward', 'foundation', 'frame', 'frankly',
         'free', 'freedom', 'freeway', 'freeze', 'freezer', 'frequent', 'frequently', 'fresh', 'fridge', 'friend',
         'friendly', 'friendship', 'frightened', 'from', 'front', 'fruit', 'fry', 'fuel', 'fulfil', 'full', 'fully',
         'fun', 'function', 'fund', 'fundamental', 'funeral', 'funny', 'furniture', 'further', 'fuss', 'future', 'gain',
         'gallery', 'game', 'gang', 'gap', 'garage', 'garbage', 'garden', 'garlic', 'gas', 'gasoline', 'gate', 'gather',
         'gay', 'gear', 'gene', 'general', 'generally', 'generate', 'generation', 'generous', 'gentle', 'gentleman',
         'gently', 'genuine', 'get', 'giant', 'gift', 'girl', 'girlfriend', 'give', 'glad', 'glance', 'glass', 'global',
         'glove', 'go', 'goal', 'god', 'gold', 'golden', 'golf', 'good', 'goodbye', 'goodness', 'goods', 'gorgeous',
         'gosh', 'govern', 'government', 'governor', 'grab', 'grade', 'gradually', 'gram', 'grammar', 'grand',
         'grandad', 'grandfather', 'grandma', 'grandmother', 'grandpa', 'granny', 'grant', 'graph', 'grass', 'grateful',
         'great', 'greatly', 'green', 'grey', 'grocery', 'gross', 'ground', 'group', 'grow', 'growth', 'guarantee',
         'guard', 'guess', 'guest', 'guidance', 'guide', 'guilty', 'guitar', 'gun', 'guy', 'habit', 'hair', 'half',
         'halfway', 'hall', 'hand', 'handbag', 'handle', 'handy', 'hang', 'happen', 'happy', 'hard', 'hardly', 'harm',
         'hat', 'hate', 'have', 'he', 'head', 'headquarters', 'health', 'healthy', 'hear', 'hearing', 'heart', 'heat',
         'heater', 'heating', 'heaven', 'heavily', 'heavy', 'height', 'hell', 'hello', 'help', 'helpful', 'hence',
         'her', 'here', 'hero', 'hers', 'herself', 'hesitate', 'hi', 'hide', 'high', 'highlight', 'highly', 'highway',
         'hill', 'him', 'himself', 'hire', 'his', 'historian', 'historical', 'history', 'hit', 'hold', 'holder',
         'holding', 'hole', 'holiday', 'holy', 'home', 'homework', 'honest', 'honestly', 'honey', 'honour', 'hook',
         'hope', 'hopefully', 'hopeless', 'horrible', 'horror', 'horse', 'hospital', 'host', 'hot', 'hotel', 'hour',
         'house', 'household', 'housing', 'how', 'however', 'huge', 'human', 'hungry', 'hunt', 'hurry', 'hurt',
         'husband', 'ice', 'idea', 'ideal', 'ideally', 'identify', 'identity', 'idiot', 'if', 'ignore', 'ill',
         'illegal', 'illness', 'illustrate', 'image', 'imagination', 'imagine', 'immediate', 'immediately', 'impact',
         'implement', 'implication', 'imply', 'import', 'importance', 'important', 'impose', 'impossible', 'impress',
         'impression', 'impressive', 'improve', 'improvement', 'in', 'inch', 'incident', 'include', 'including',
         'income', 'incorporate', 'increase', 'increasingly', 'incredible', 'incredibly', 'indeed', 'independence',
         'independent', 'index', 'indicate', 'indication', 'individual', 'industrial', 'industry', 'inevitable',
         'inevitably', 'infant', 'infection', 'inflation', 'influence', 'inform', 'informal', 'information', 'initial',
         'initially', 'initiative', 'injure', 'injury', 'inner', 'innocent', 'innovation', 'input', 'inquiry', 'insect',
         'inside', 'insist', 'inspection', 'inspector', 'install', 'instance', 'instant', 'instead', 'institute',
         'institution', 'instruction', 'instrument', 'insurance', 'intellectual', 'intelligence', 'intelligent',
         'intend', 'intense', 'intention', 'interaction', 'interest', 'interested', 'interesting', 'interjection',
         'internal', 'international', 'internet', 'interpret', 'interpretation', 'interval', 'intervention',
         'interview', 'into', 'introduce', 'introduction', 'invest', 'investigate', 'investigation', 'investment',
         'invite', 'involve', 'involved', 'involvement', 'iron', 'island', 'issue', 'it', 'item', 'its', 'itself',
         'jacket', 'jam', 'job', 'join', 'joint', 'joke', 'journalist', 'journey', 'joy', 'judge', 'judgment', 'juice',
         'jump', 'jumper', 'junior', 'jury', 'just', 'justice', 'justify', 'keen', 'keep', 'kettle', 'key', 'keyboard',
         'kick', 'kid', 'kill', 'kilometre', 'kind', 'king', 'kiss', 'kit', 'kitchen', 'knee', 'knife', 'knock', 'know',
         'knowledge', 'known', 'lab', 'label', 'laboratory', 'labour', 'lack', 'lad', 'ladder', 'lady', 'lake', 'lamb',
         'lamp', 'land', 'landlord', 'landscape', 'lane', 'language', 'large', 'largely', 'last', 'late', 'later',
         'latter', 'laugh', 'launch', 'law', 'lawyer', 'lay', 'layer', 'lazy', 'lead', 'leader', 'leadership',
         'leading', 'leaf', 'league', 'lean', 'learn', 'least', 'leather', 'leave', 'lecture', 'left', 'leg', 'legal',
         'legislation', 'leisure', 'lend', 'length', 'less', 'lesson', 'let', 'letter', 'level', 'liberal', 'library',
         'licence', 'lick', 'lid', 'lie', 'life', 'lift', 'light', 'lighting', 'like', 'likely', 'limit', 'limitation',
         'limited', 'line', 'link', 'lip', 'liquid', 'list', 'listen', 'literally', 'literary', 'literature', 'little',
         'live', 'lively', 'living', 'load', 'loan', 'local', 'locate', 'location', 'lock', 'log', 'logical', 'lonely',
         'long', 'long-term', 'look', 'loose', 'lord', 'lorry', 'lose', 'loss', 'lost', 'lot', 'loud', 'lounge', 'love',
         'lovely', 'lover', 'low', 'lower', 'luck', 'luckily', 'lucky', 'lump', 'lunch', 'lunchtime', 'machine',
         'machinery', 'mad', 'madam', 'magazine', 'magic', 'mail', 'main', 'mainly', 'maintain', 'maintenance', 'major',
         'majority', 'make', 'male', 'mall', 'man', 'manage', 'management', 'manager', 'manner', 'manufacturer',
         'manufacturing', 'many', 'map', 'march', 'margin', 'mark', 'market', 'marketing', 'marriage', 'married',
         'marry', 'marvellous', 'mass', 'massive', 'master', 'match', 'mate', 'material', 'math', 'maths', 'matter',
         'maximum', 'may', 'maybe', 'me', 'meal', 'mean', 'meaning', 'means', 'meanwhile', 'measure', 'measurement',
         'meat', 'mechanism', 'media', 'medical', 'medicine', 'medieval', 'medium', 'meet', 'meeting', 'member',
         'membership', 'memory', 'mental', 'mention', 'menu', 'mere', 'merely', 'mess', 'message', 'messy', 'metal',
         'method', 'metre', 'middle', 'midnight', 'might', 'mile', 'military', 'milk', 'millimetre', 'mind', 'mine',
         'mineral', 'minimum', 'minister', 'ministry', 'minor', 'minority', 'minute', 'mirror', 'misery', 'miss',
         'mission', 'mistake', 'mix', 'mixed', 'mixture', 'mobile', 'mode', 'model', 'modern', 'mom', 'moment', 'mommy',
         'money', 'monitor', 'month', 'mood', 'moon', 'moral', 'more', 'moreover', 'morning', 'mortgage', 'most',
         'mostly', 'mother', 'motion', 'motor', 'motorway', 'mountain', 'mouse', 'mouth', 'move', 'movement', 'movie',
         'much', 'mud', 'mum', 'mummy', 'murder', 'muscle', 'museum', 'mushroom', 'music', 'musical', 'must', 'my',
         'myself', 'mystery', 'nail', 'naked', 'name', 'narrow', 'nasty', 'nation', 'national', 'native', 'natural',
         'naturally', 'nature', 'naughty', 'near', 'nearby', 'nearly', 'neat', 'necessarily', 'necessary', 'neck',
         'need', 'negative', 'negotiate', 'negotiation', 'neighbour', 'neighbourhood', 'neither', 'nerve', 'nervous',
         'net', 'network', 'never', 'nevertheless', 'new', 'newly', 'news', 'newspaper', 'next', 'nice', 'nicely',
         'night', 'nil', 'no', 'nobody', 'nod', 'noise', 'noisy', 'none', 'nonsense', 'nope', 'nor', 'normal',
         'normally', 'north', 'northern', 'nose', 'not', 'notably', 'note', 'nothing', 'notice', 'notion', 'novel',
         'now', 'nowadays', 'nowhere', 'nuclear', 'nuisance', 'number', 'numerous', 'nurse', 'nut', 'object',
         'objection', 'objective', 'obligation', 'observation', 'observe', 'obtain', 'obvious', 'obviously', 'occasion',
         'occasional', 'occasionally', 'occupation', 'occupy', 'occur', 'ocean', 'odd', 'odds', 'of', 'off', 'offence',
         'offer', 'office', 'officer', 'official', 'often', 'oil', 'old', 'on', 'once', 'one', 'onion', 'only', 'onto',
         'open', 'opening', 'operate', 'operation', 'operator', 'opinion', 'opponent', 'opportunity', 'oppose',
         'opposite', 'opposition', 'option', 'or', 'orange', 'order', 'ordinary', 'organ', 'organic', 'organization',
         'organize', 'organized', 'origin', 'original', 'originally', 'other', 'otherwise', 'ought', 'ounce', 'our',
         'ours', 'ourselves', 'out', 'outcome', 'output', 'outside', 'outstanding', 'oven', 'over', 'overall',
         'overcome', 'overseas', 'overtime', 'owe', 'own', 'owner', 'ownership', 'o’clock', 'pace', 'pack', 'package',
         'packet', 'pad', 'page', 'pain', 'paint', 'painting', 'pair', 'palace', 'pale', 'pan', 'panel', 'panic',
         'pants', 'paper', 'parcel', 'pardon', 'parent', 'park', 'parking', 'parliament', 'part', 'participate',
         'particular', 'particularly', 'partly', 'partner', 'partnership', 'party', 'pass', 'passage', 'passenger',
         'passion', 'past', 'path', 'patience', 'patient', 'pattern', 'pause', 'pay', 'payment', 'peace', 'peaceful',
         'peak', 'pen', 'penalty', 'pencil', 'penny', 'pension', 'people', 'pepper', 'per', 'perceive', 'percent',
         'percentage', 'perception', 'perfect', 'perfectly', 'perform', 'performance', 'perhaps', 'period', 'permanent',
         'permission', 'permit', 'person', 'personal', 'personality', 'personally', 'personnel', 'perspective',
         'persuade', 'petrol', 'phase', 'philosophy', 'phone', 'photo', 'photocopy', 'photograph', 'phrase', 'physical',
         'physically', 'physics', 'piano', 'pick', 'picture', 'pie', 'piece', 'pig', 'pile', 'pill', 'pilot', 'pin',
         'pink', 'pint', 'pipe', 'pitch', 'pity', 'pizza', 'place', 'plain', 'plan', 'plane', 'planet', 'plant',
         'plastic', 'plate', 'platform', 'play', 'player', 'pleasant', 'please', 'pleased', 'pleasure', 'plenty',
         'plot', 'plug', 'plus', 'pocket', 'poem', 'poet', 'poetry', 'point', 'pole', 'police', 'policeman', 'policy',
         'polite', 'political', 'politician', 'politics', 'poll', 'pollution', 'pond', 'pool', 'poor', 'pop', 'popular',
         'population', 'port', 'pose', 'position', 'positive', 'possess', 'possession', 'possibility', 'possible',
         'possibly', 'post', 'poster', 'pot', 'potato', 'potential', 'pound', 'pour', 'poverty', 'power', 'powerful',
         'practical', 'practically', 'practice', 'practise', 'praise', 'pray', 'prayer', 'precise', 'precisely',
         'predict', 'prefer', 'preference', 'pregnant', 'premise', 'preparation', 'prepare', 'prepared', 'presence',
         'present', 'presentation', 'preserve', 'president', 'press', 'pressure', 'presumably', 'presume', 'pretend',
         'pretty', 'prevent', 'previous', 'previously', 'price', 'pride', 'priest', 'primarily', 'primary', 'prince',
         'princess', 'principal', 'principle', 'print', 'printer', 'prior', 'priority', 'prison', 'prisoner', 'private',
         'privilege', 'prize', 'probably', 'problem', 'procedure', 'proceed', 'proceeding', 'process', 'produce',
         'producer', 'product', 'production', 'profession', 'professional', 'professor', 'profile', 'profit', 'program',
         'programme', 'progress', 'project', 'promise', 'promote', 'promotion', 'prompt', 'proof', 'proper', 'properly',
         'property', 'proportion', 'proposal', 'propose', 'proposed', 'prosecution', 'prospect', 'protect',
         'protection', 'protest', 'proud', 'prove', 'provide', 'provided', 'providing', 'provision', 'psychological',
         'psychology', 'pub', 'public', 'publication', 'publicity', 'publish', 'publisher', 'pudding', 'pull', 'punch',
         'punishment', 'pupil', 'purchase', 'pure', 'purely', 'purple', 'purpose', 'purse', 'pursue', 'push', 'put',
         'qualification', 'qualify', 'quality', 'quantity', 'quarter', 'queen', 'question', 'queue', 'quick', 'quickly',
         'quid', 'quiet', 'quietly', 'quit', 'quite', 'quote', 'race', 'racing', 'radical', 'radio', 'rail', 'railway',
         'rain', 'raise', 'range', 'rank', 'rapid', 'rapidly', 'rare', 'rarely', 'rate', 'rather', 'ratio', 'raw',
         'reach', 'react', 'reaction', 'read', 'reader', 'readily', 'reading', 'ready', 'real', 'realistic', 'reality',
         'realize', 'really', 'reason', 'reasonable', 'reasonably', 'recall', 'receipt', 'receive', 'recent',
         'recently', 'reception', 'recipe', 'reckon', 'recognition', 'recognize', 'recommend', 'recommendation',
         'record', 'recording', 'recover', 'recovery', 'red', 'reduce', 'reduction', 'refer', 'reference', 'reflect',
         'reflection', 'reform', 'refrigerator', 'refuse', 'regard', 'regime', 'region', 'regional', 'register',
         'registration', 'regret', 'regular', 'regularly', 'regulation', 'reinforce', 'reject', 'relate', 'related',
         'relation', 'relationship', 'relative', 'relatively', 'relax', 'release', 'relevant', 'relief', 'relieve',
         'religion', 'religious', 'rely', 'remain', 'remaining', 'remains', 'remark', 'remarkable', 'remember',
         'remind', 'remote', 'remove', 'rent', 'repair', 'repeat', 'replace', 'replacement', 'reply', 'report',
         'reporter', 'represent', 'representation', 'representative', 'republic', 'reputation', 'request', 'require',
         'requirement', 'rescue', 'research', 'reserve', 'resident', 'residential', 'resign', 'resignation', 'resist',
         'resistance', 'resolution', 'resolve', 'resort', 'resource', 'respect', 'respectively', 'respond', 'response',
         'responsibility', 'responsible', 'rest', 'restaurant', 'restore', 'restrict', 'restriction', 'result',
         'retain', 'retire', 'retirement', 'return', 'reveal', 'revenue', 'reverse', 'review', 'revolution', 'reward',
         'rhythm', 'rice', 'rich', 'rid', 'ride', 'ridiculous', 'right', 'ring', 'rip', 'rise', 'risk', 'rival',
         'river', 'road', 'rob', 'rock', 'role', 'roll', 'roof', 'room', 'root', 'rope', 'rough', 'roughly', 'round',
         'route', 'routine', 'row', 'royal', 'rub', 'rubber', 'rubbish', 'rude', 'ruin', 'rule', 'run', 'rural', 'rush',
         'sack', 'sad', 'safe', 'safety', 'sail', 'sake', 'salad', 'salary', 'sale', 'salt', 'same', 'sample', 'sand',
         'sandwich', 'satellite', 'satisfaction', 'satisfied', 'satisfy', 'sauce', 'sausage', 'save', 'saving', 'say',
         'scale', 'scared', 'scene', 'schedule', 'scheme', 'school', 'science', 'scientific', 'scientist', 'scope',
         'score', 'scratch', 'scream', 'screen', 'screw', 'script', 'sea', 'seal', 'search', 'season', 'seat', 'second',
         'secondary', 'secondly', 'secret', 'secretary', 'section', 'sector', 'secure', 'security', 'see', 'seed',
         'seek', 'seem', 'seize', 'select', 'selection', 'self', 'sell', 'send', 'senior', 'sense', 'sensible',
         'sensitive', 'sentence', 'separate', 'sequence', 'series', 'serious', 'seriously', 'servant', 'serve',
         'service', 'session', 'set', 'setting', 'settle', 'settlement', 'several', 'severe', 'sew', 'sex', 'sexual',
         'shadow', 'shake', 'shall', 'shame', 'shape', 'share', 'sharp', 'sharply', 'shave', 'she', 'shed', 'sheep',
         'sheet', 'shelf', 'shell', 'shelter', 'shift', 'shine', 'ship', 'shirt', 'shock', 'shocked', 'shocking',
         'shoe', 'shoot', 'shop', 'shopping', 'short', 'shortly', 'shot', 'should', 'shoulder', 'shout', 'shove',
         'show', 'shower', 'shrug', 'shut', 'sick', 'side', 'sight', 'sign', 'signal', 'signature', 'significance',
         'significant', 'significantly', 'silence', 'silent', 'silly', 'silver', 'similar', 'similarly', 'simple',
         'simply', 'sin', 'since', 'sing', 'singer', 'single', 'sink', 'sir', 'sister', 'sit', 'site', 'situation',
         'size', 'skill', 'skin', 'skirt', 'sky', 'sleep', 'slice', 'slide', 'slight', 'slightly', 'slim', 'slip',
         'slope', 'slow', 'slowly', 'small', 'smart', 'smell', 'smile', 'smoke', 'smoking', 'smooth', 'snap', 'snow',
         'so', 'so-called', 'soap', 'social', 'society', 'sock', 'soft', 'software', 'soil', 'soldier', 'sole',
         'solicitor', 'solid', 'solution', 'solve', 'some', 'somebody', 'somehow', 'someone', 'something', 'sometimes',
         'somewhat', 'somewhere', 'son', 'song', 'soon', 'sore', 'sorry', 'sort', 'soul', 'sound', 'soup', 'source',
         'south', 'southern', 'space', 'spare', 'speak', 'speaker', 'special', 'specialist', 'species', 'specific',
         'specifically', 'specify', 'speech', 'speed', 'spell', 'spelling', 'spend', 'spill', 'spin', 'spirit',
         'spiritual', 'spite', 'split', 'spoil', 'spokesman', 'spoon', 'sport', 'spot', 'spray', 'spread', 'spring',
         'squad', 'square', 'squeeze', 'stable', 'staff', 'stage', 'stair', 'stake', 'stall', 'stamp', 'stand',
         'standard', 'star', 'stare', 'start', 'starve', 'state', 'statement', 'station', 'statistic', 'status', 'stay',
         'steady', 'steak', 'steal', 'steam', 'steel', 'steep', 'step', 'stick', 'stiff', 'still', 'stir', 'stock',
         'stomach', 'stone', 'stop', 'storage', 'store', 'storm', 'story', 'straight', 'straightforward', 'strain',
         'strange', 'stranger', 'strategic', 'strategy', 'straw', 'strawberry', 'stream', 'street', 'strength',
         'strengthen', 'stress', 'stretch', 'strict', 'strike', 'string', 'strip', 'stroke', 'strong', 'strongly',
         'structure', 'struggle', 'student', 'studio', 'study', 'stuff', 'stupid', 'style', 'subject', 'submit',
         'subsequent', 'subsequently', 'substance', 'substantial', 'succeed', 'success', 'successful', 'successfully',
         'such', 'suck', 'sudden', 'suddenly', 'suffer', 'sufficient', 'sugar', 'suggest', 'suggestion', 'suit',
         'suitable', 'sum', 'summer', 'sun', 'super', 'supermarket', 'supper', 'supply', 'support', 'supporter',
         'suppose', 'sure', 'surely', 'surface', 'surgery', 'surprise', 'surprised', 'surprising', 'surprisingly',
         'surround', 'survey', 'survival', 'survive', 'suspect', 'suspicion', 'suspicious', 'sustain', 'swap', 'swear',
         'sweep', 'sweet', 'swim', 'swimming', 'swing', 'switch', 'symbol', 'sympathy', 'system', 'table', 'tablet',
         'tackle', 'tail', 'take', 'tale', 'talent', 'talk', 'tall', 'tank', 'tap', 'tape', 'target', 'task', 'taste',
         'tax', 'taxi', 'tea', 'teach', 'teacher', 'teaching', 'team', 'tear', 'technical', 'technique', 'technology',
         'telephone', 'television', 'tell', 'telly', 'temperature', 'temporary', 'tend', 'tendency', 'tennis',
         'tension', 'tent', 'term', 'terrible', 'terribly', 'territory', 'terror', 'terrorist', 'test', 'text', 'than',
         'thank', 'thanks', 'that', 'the', 'theatre', 'their', 'theirs', 'them', 'theme', 'themselves', 'then',
         'theoretical', 'theory', 'there', 'therefore', 'they', 'thick', 'thin', 'thing', 'think', 'this', 'though',
         'thought', 'threat', 'threaten', 'three', 'throat', 'through', 'throughout', 'throw', 'thus', 'ticket', 'tidy',
         'tie', 'tight', 'tile', 'till', 'time', 'tin', 'tiny', 'tip', 'tired', 'title', 'to', 'toast', 'today', 'toe',
         'together', 'toilet', 'tomato', 'tomorrow', 'ton', 'tone', 'tongue', 'tonight', 'too', 'tool', 'tooth', 'top',
         'topic', 'total', 'totally', 'touch', 'tough', 'tour', 'tourist', 'towards', 'towel', 'tower', 'town', 'toy',
         'track', 'trade', 'tradition', 'traditional', 'traffic', 'trailer', 'train', 'trainer', 'training',
         'transaction', 'transfer', 'transform', 'transition', 'translate', 'transport', 'transportation', 'trash',
         'travel', 'tray', 'treat', 'treatment', 'treaty', 'tree', 'tremendous', 'trend', 'trial', 'trick', 'tricky',
         'trip', 'troop', 'trouble', 'trousers', 'truck', 'true', 'truly', 'trust', 'truth', 'try', 'tube', 'tune',
         'tunnel', 'turn', 'twice', 'twist', 'type', 'typical', 'tyre', 'ugly', 'ultimate', 'ultimately', 'unable',
         'unbelievable', 'uncle', 'under', 'underneath', 'understand', 'understanding', 'undertake', 'unemployed',
         'unemployment', 'unfair', 'unfortunate', 'unfortunately', 'unhappy', 'uniform', 'union', 'unique', 'unit',
         'united', 'unity', 'universal', 'universe', 'university', 'unknown', 'unless', 'unlike', 'unlikely', 'until',
         'unusual', 'up', 'upon', 'upper', 'upset', 'upstairs', 'urban', 'urge', 'urgent', 'us', 'use', 'used',
         'useful', 'user', 'usual', 'usually', 'vacation', 'vague', 'valley', 'valuable', 'value', 'van', 'variation',
         'variety', 'various', 'vary', 'vast', 'vegetable', 'vehicle', 'version', 'very', 'vet', 'via', 'victim',
         'victory', 'video', 'view', 'village', 'violence', 'violent', 'virtually', 'virtue', 'virus', 'visible',
         'vision', 'visit', 'visitor', 'visual', 'vital', 'voice', 'volume', 'voluntary', 'vote', 'vulnerable', 'wage',
         'wait', 'wake', 'walk', 'wall', 'want', 'war', 'ward', 'wardrobe', 'warm', 'warn', 'warning', 'wash',
         'washing', 'waste', 'watch', 'water', 'wave', 'way', 'we', 'weak', 'weakness', 'wealth', 'weapon', 'wear',
         'weather', 'web', 'website', 'wedding', 'week', 'weekend', 'weekly', 'weigh', 'weight', 'weird', 'welcome',
         'welfare', 'well', 'west', 'western', 'wet', 'what', 'whatever', 'whatsoever', 'wheel', 'when', 'whenever',
         'where', 'whereas', 'wherever', 'whether', 'which', 'while', 'whisky', 'whisper', 'white', 'who', 'whoever',
         'whole', 'whom', 'whose', 'why', 'wicked', 'wide', 'widely', 'widespread', 'wife', 'wild', 'will', 'willing',
         'win', 'wind', 'window', 'windy', 'wine', 'wing', 'winner', 'winter', 'wipe', 'wire', 'wise', 'wish', 'with',
         'withdraw', 'within', 'without', 'witness', 'woman', 'wonder', 'wonderful', 'wood', 'wooden', 'wool', 'word',
         'work', 'worker', 'working', 'workshop', 'world', 'worried', 'worry', 'worrying', 'worse', 'worth', 'would',
         'wound', 'wrap', 'write', 'writer', 'writing', 'wrong', 'yard', 'yeah', 'year', 'yellow', 'yep', 'yes',
         'yesterday', 'yet', 'you', 'young', 'youngster', 'your', 'yours', 'yourself', 'youth', 'zone']
        )

    def generate(self) -> List[TestCase]:
        list_tests = [
            TestCase(stdin='all',
                     attach=TestClue('108', '25', '6', 580, 196, 20, 12.86, 12.84, 13.56, 14.13, 8.18, 22.0),
                     args=["--infile", "in.txt", "--words", "words.txt"],
                     files={
                         "in.txt": "Readability is " +
                                   "the ease with which a reader can " +
                                   "understand a written text. In natural " +
                                   "language, the readability of text depends " +
                                   "on its content and its presentation. " +
                                   "Researchers have used various factors " +
                                   "to measure readability. Readability is " +
                                   "more than simply legibility, which is a " +
                                   "measure of how easily a reader can distinguish " +
                                   "individual letters or characters from each other. " +
                                   "Higher readability eases reading effort and speed " +
                                   "for any reader, but it is especially important for " +
                                   "those who do not have high reading comprehension. " +
                                   "In readers with poor reading comprehension, raising " +
                                   "the readability level of a text from mediocre to good " +
                                   "can make the difference between success and failure",
                         self.file_words: self.words
                     }),

            TestCase(stdin='all',
                     attach=TestClue('100', '33', '10', 476, 154, 12, 5.99, 6.31, 9.42, 10.66, 9.34, 15.4),
                     args=["--infile", "in.txt", "--words", "words.txt"],
                     files={
                         "in.txt": "This is the page of the Simple English Wikipedia. " +
                                   "A place where people work together to write encyclopedias " +
                                   "in different languages. That includes children and adults " +
                                   "who are learning English. There are 142,262 articles on the " +
                                   "Simple English Wikipedia. All of the pages are free to use. " +
                                   "They have all been published under both the Creative Commons" +
                                   " License 3 and the GNU Free Documentation License. " +
                                   "You can help here! You may change these pages and make new " +
                                   "pages. Read the help pages and other good pages to learn " +
                                   "how to write pages here. You may ask questions at Simple talk.",
                         self.file_words: self.words
                     }),

            TestCase(stdin='all',
                     attach=TestClue('112', '33', '6', 505, 167, 8, 9.14, 9.28, 9.73, 9.13, 9.3, 16.8),
                     args=["--infile", "in.txt", "--words", "words.txt"],
                     files={
                         "in.txt": "Frequency is how often an event repeats itself over a set amount of time. In physics, the frequency of a wave is the number of wave crests that pass a point in one second (a wave crest is the peak of the wave). Hertz is the unit of frequency. All electromagnetic waves travel at the speed of light in a vacuum but they travel at slower speeds when they travel through a medium that is not a vacuum. Other waves, such as sound waves, travel at much much lower speeds and can not travel through a vacuum. Examples of electromagnetic waves are: light waves, radio waves, infrared radiation, microwaves, and gamma waves.",
                         self.file_words: self.words
                     })
        ]

        return list_tests

    def check(self, reply: str, attach) -> CheckResult:

        found_words = False
        found_sentences = False
        found_diffs = False
        found_chars = False
        found_syllables = False
        found_polysyllables = False

        found_ari = False
        found_fkt = False
        found_smg = False
        found_cli = False
        found_prob_score = False
        found_age = False

        for stroka in reply.lower().split('\n'):
            if "words:" in stroka and "difficult" not in stroka:
                found_words = True
                if attach.words not in stroka:
                    return CheckResult.wrong("Wrong number of words")

            if "sentences:" in stroka:
                found_sentences = True
                if attach.sentences not in stroka:
                    return CheckResult.wrong("Wrong number of sentences")

            if "difficult words:" in stroka:
                found_diffs = True
                if attach.diffs not in stroka:
                    return CheckResult.wrong("Wrong number of difficult words")

            if "characters:" in stroka:
                found_chars = True
                try:
                    user_characters = int(stroka.split(':')[-1])
                except ValueError:
                    return CheckResult.wrong("Can't parse characters count!"
                                             "\nYour output format should be like in examples.")
                if abs(user_characters - attach.characters) > 10:
                    return CheckResult.wrong(f"Wrong number of characters. "
                                             f"Should be {attach.characters}, but found {user_characters}")

            if "polysyllables:" in stroka:
                found_polysyllables = True
                try:
                    user_polysyllables = int(stroka.split(':')[-1])
                except ValueError:
                    return CheckResult.wrong("Can't parse polysyllables count!"
                                             "\nYour output format should be like in examples.")
                if abs(user_polysyllables - attach.polysyllables) > 5:
                    return CheckResult.wrong(f"Wrong number of polysyllables. "
                                             f"Should be {attach.polysyllables}, but found {user_polysyllables}")

            if "syllables:" in stroka and "poly" not in stroka:
                found_syllables = True
                try:
                    user_syllables = int(stroka.split(':')[-1])
                except ValueError:
                    return CheckResult.wrong("Can't parse syllables count!"
                                             "\nYour output format should be like in examples.")
                if abs(user_syllables - attach.syllables) > 20:
                    return CheckResult.wrong(f"Wrong number of syllables. "
                                             f"Should be {attach.syllables}, but found {user_syllables}")

            if "enter the score" not in reply.lower():
                return CheckResult.wrong("The program should offer a user to choose the  metrics")

            if stroka.startswith("automated readability index"):
                found_ari = True
                rounded = int(attach.ari)
                actual = str(rounded)
                before = str(rounded - 1)
                after = str(rounded + 1)
                if not (actual in stroka or before in stroka or after in stroka):
                    return CheckResult.wrong(f"Wrong Automated Readability Index score. Should be around {attach.ari}),"
                                             f" your output: \n {stroka}")
                if "year" not in stroka or "old" not in stroka:
                    return CheckResult.wrong("No age in Automated Readability Index")

            if stroka.startswith("flesch–kincaid"):
                found_fkt = True
                rounded = int(attach.fkri)
                actual = str(rounded)
                before = str(rounded - 1)
                after = str(rounded + 1)
                if not (actual in stroka or before in stroka or after in stroka):
                    return CheckResult.wrong(f"Wrong Flesch–Kincaid score. Should be around {attach.fkri}),"
                                             f" your output: \n {stroka}")
                if "year" not in stroka or "old" not in stroka:
                    return CheckResult.wrong("No age in Flesch–Kincaid")

            if stroka.startswith("simple measure of gobbledygook"):
                found_smg = True
                rounded = int(attach.smog)
                actual = str(rounded)
                before = str(rounded - 1)
                after = str(rounded + 1)
                if not (actual in stroka or before in stroka or after in stroka):
                    return CheckResult.wrong(
                        f"Wrong Simple Measure of Gobbledygook score. Should be around {attach.smog}),"
                        f" your output: \n {stroka}")
                if "year" not in stroka or "old" not in stroka:
                    return CheckResult.wrong("No age in Simple Measure of Gobbledygook")

            if stroka.startswith("coleman–liau"):
                found_cli = True
                rounded = int(attach.cli)
                actual = str(rounded)
                before = str(rounded - 1)
                after = str(rounded + 1)
                if not (actual in stroka or before in stroka or after in stroka):
                    return CheckResult.wrong(f"Wrong Coleman–Liau score. Should be around {attach.cli}),"
                                             f" your output: \n {stroka}")
                if "year" not in stroka or "old" not in stroka:
                    return CheckResult.wrong("No age in Coleman–Liau")

            if "probability-based" in stroka.lower():
                found_prob_score = True
                try:
                    user_score = float(stroka.split(':')[-1].split('(')[0])
                except ValueError:
                    return CheckResult.wrong("Can't parse the score!"
                                             "\nYour output format should be like in examples.")
                if abs(user_score - attach.prob_score) > 0.2:
                    return CheckResult.wrong("Wrong probability-based score")

            # print("stroka", stroka)
            if "year" in stroka and "old" in stroka and 'average' in stroka:
                found_age = True
                try:
                    print("stroka", stroka)
                    user_age = float(stroka.split()[-1].split('-')[0])
                except ValueError:
                    return CheckResult.wrong("Can't parse the age!"
                                             "\nYour output format should be like in examples.")
                if abs(user_age - attach.age) > 1.5:
                    return CheckResult.wrong("Wrong age")

        if not found_words:
            return CheckResult.wrong("There is no words amount")
        if not found_sentences:
            return CheckResult.wrong("There is no sentences amount")
        if not found_diffs:
            return CheckResult.wrong("There is no amount of difficult words")
        if not found_chars:
            return CheckResult.wrong("There is no characters amount")
        if not found_polysyllables:
            return CheckResult.wrong("There is no polysyllables in output")
        if not found_syllables:
            return CheckResult.wrong("There is no syllables in output")
        if not found_ari:
            return CheckResult.wrong("There is no Automated Readability Index in output")
        if not found_fkt:
            return CheckResult.wrong("There is no Flesch–Kincaid readability tests in output")
        if not found_smg:
            return CheckResult.wrong("There is no Simple Measure of Gobbledygook in output")
        if not found_cli:
            return CheckResult.wrong("There is no Coleman–Liau index in output")
        if not found_prob_score:
            return CheckResult.wrong("There is no Probability score in output")
        if not found_age:
            return CheckResult.wrong("There is no age in output")

        return CheckResult.correct()


if __name__ == '__main__':
    TestTheFifth('readability.readability').run_tests()