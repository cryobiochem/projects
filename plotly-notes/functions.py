# Create a list of cationic, anionic, and uncharged monomers as an alternative to parameter nesting
def polarity (monomer, charge):

    cationic = list()
    anionic = list()
    nonionic = list()

    for i in db2.index:
        monomer = db2['short name'][i]
        charge = db2['Physiological Charge'][i]
        if charge == -1:
            anionic.append(monomer)
        elif charge == 1:
            cationic.append(monomer)
        else:
            nonionic.append(monomer)

    print('Positively charged monomers:', ', '.join(cationic))
    print('Negatively charged monomers:', ', '.join(anionic))
    print('Uncharged monomers:', ', '.join(nonionic))

# Transform absolute data in axis to % of max
def percentage(part, whole):
  return 100 * float(part) / float(whole)
