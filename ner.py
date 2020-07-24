import spacy
import time

def fmt_time(secs):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    res=[]
    if(h):
        res.append("{:.0f}h".format(h))
    if(m):
        res.append("{:.0f}m".format(m))
    res.append("{:.02f}s".format(s))
    return " ".join(res)

def status(t0, count, total):
    t1 = time.time() - t0
    exp_t = (t1 / (count)) * total - t1
    return f"Processed:{count}/{total} ({round(100 * count / total, 2)}%)" + f". Time Taken: {fmt_time(t1)}" + f". Expected Completion: {fmt_time(exp_t)}"

def print_continous(text):
    print(" "*1000+"\r"+text,end="\r")

class NER:
    def __init__(self,model):
        self.nlp_model=spacy.load(model)

    def extract_ent_info(self,doc):
        return [{"text": e.text, "type": e.label_, "st": e.start_char, "en": e.end_char, "tk_st": e.start, "tk_len": len(e)} for e in self.nlp_model(doc).ents]

    def spacy_ner(self,docs,verbose=False):
        t0=time.time()
        entity_mentions=[]
        entity_count=0
        if(type(docs)==str):
            entity_mentions=self.extract_ent_info(docs)
            if(verbose):
                total,count=1,1
            entity_count=len(entity_mentions)
        else:
            t0=time.time()
            total=len(docs)
            count=0
            for d in docs:
                rec=self.extract_ent_info(d)
                entity_mentions.append(rec)
                entity_count+=len(rec)
                count+=1
                if(verbose and count%10==0):
                    print_continous(status(t0,count,total))
        if(verbose):
            print_continous(status(t0,count,total))
            print(f"\nTotal Entities Found: {entity_count}")
        return entity_mentions