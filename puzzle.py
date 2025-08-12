from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Structure: Each person is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    
    # What A said: "I am both a knight and a knave"
    # If A is a knight, then what A said is true
    # If A is a knave, then what A said is false
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Structure: Each person is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    
    # What A said: "We are both knaves"
    # If A is a knight, then what A said is true
    # If A is a knave, then what A said is false
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Structure: Each person is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    
    # What A said: "We are the same kind"
    # Same kind means both knights or both knaves
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    
    # What B said: "We are of different kinds"
    # Different kinds means one knight, one knave
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Structure: Each person is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    
    # We need to model what A actually said
    # Let's use symbols for A's possible statements
    # Since A said either "I am a knight" or "I am a knave", exactly one is true
    
    # Let's think about this differently:
    # If A said "I am a knight":
    #   - If A is a knight, the statement is true (consistent)
    #   - If A is a knave, the statement is false (consistent)
    # If A said "I am a knave":
    #   - If A is a knight, the statement is false (contradicts knight telling truth)
    #   - If A is a knave, the statement is true (contradicts knave telling lies)
    # So A could not have said "I am a knave" - this is impossible
    # Therefore A must have said "I am a knight"
    
    # Since we know A said "I am a knight" (the only possibility):
    # This statement is true if A is a knight, false if A is a knave
    # But this doesn't give us additional constraints beyond the basic structure
    
    # B says "A said 'I am a knave'"
    # But we know A could not have said this (it's logically impossible)
    # So B's statement is false
    # If B is a knight, B's statement would be true (contradiction)
    # If B is a knave, B's statement is false (consistent)
    # We can model this by saying: if B is knight, then A said "I am a knave"
    # But since A could never say "I am a knave", this forces B to be a knave
    
    # Let ASaidKnave represent "A said 'I am a knave'"
    # We know this is impossible, so ASaidKnave is always False
    # But we can let the model checker figure this out
    
    # Alternative approach: directly model the logical impossibility
    # B claims A said "I am a knave"
    # For B to be telling the truth, A must have said "I am a knave"
    # But "I am a knave" creates a paradox (can never be said)
    # So B must be lying, making B a knave
    
    # B's first statement: "A said 'I am a knave'"
    # We model this as: if B is knight, then [what B claims is true]
    # But what B claims (A said "I am a knave") is impossible
    # We can model the impossibility by noting that:
    # - If A is knight and said "I am a knave", that's false (contradiction)
    # - If A is knave and said "I am a knave", that's true (contradiction)
    
    # Let's model it this way: B claims A said "I am a knave"
    # This means: if B is knight, then A said something that creates a paradox
    # We model the paradox: if someone says "I am a knave", then they are both knight and not knight
    Implication(BKnight, And(AKnight, AKnave)),  # This is impossible, so B cannot be knight
    
    # B's second statement: "C is a knave"
    Biconditional(BKnight, CKnave),
    
    # C's statement: "A is a knight"
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
