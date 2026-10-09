class KnowledgeBase:
    """Propositional Knowledge Base of Facts and Horn-clause Rules."""

    def __init__(self):
        self.facts = set()   # unique string facts, e.g. "TargetVisible"
        self.rules = []      # list of ( [premises], "conclusion" ) tuples

    def tell_fact(self, fact_string):
        """Add a fact (percept) to the KB."""
        self.facts.add(fact_string)

    def tell_rule(self, premise_list, conclusion_string):
        """Add a Horn clause: premise1 AND premise2 AND ... => conclusion."""
        self.rules.append((premise_list, conclusion_string))

    def clear_facts(self):
        """Remove all facts (rules are kept)."""
        self.facts.clear()

    def forward_chain(self):
        """Data-driven forward chaining using Modus Ponens.

        Keeps passing over the rules until a full pass adds no new facts.
        """
        new_facts_added = True

        while new_facts_added:
            new_facts_added = False

            for premises, conclusion in self.rules:
                if conclusion not in self.facts:
                    # Modus Ponens check: all premises must be known facts
                    if all(p in self.facts for p in premises):
                        self.facts.add(conclusion)
                        new_facts_added = True
