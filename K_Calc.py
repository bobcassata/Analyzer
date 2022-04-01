import pandas as pd
import numpy as np
import string


def analize2(file_handler2, app2):
    df = pd.read_csv(file_handler2)
    df.fillna(0)

    n_of_Raters = df.shape[0]

    grid = np.full((33, n_of_Raters), 0, dtype= int)

    print(n_of_Raters)
    #print(grid)

    ###RATERS #cant save csv with this
    #name_list = df["Name"].tolist()
    #k=0
    #while k < len(name_list):
        #for name in name_list:
            #grid[0, k]= name
            #k= k+1

    ######## FILLING GRID ########

    ###STRAT RISKS
    qual_stra= df[df["Strategic Risk"].str.contains(r"Approval of product/service delivery even if the quality goals are not met").fillna(False)].index.tolist()
    for rater in qual_stra:
        grid[1,rater] = 1
    cred_stra= df[df["Strategic Risk"].str.contains(r"Decision impacting credit, financial aspects").fillna(False)].index.tolist()
    for rater in cred_stra:
        grid[2,rater] = 1
    infra_stra= df[df["Strategic Risk"].str.contains(r"Decision impacting infrastructures availability").fillna(False)].index.tolist()
    for rater in infra_stra:
        grid[3,rater] = 1
    res_stra = df[df["Strategic Risk"].str.contains(r"Decision impacting resources and headcount").fillna(False)].index.tolist()
    for rater in res_stra:
        grid[4,rater] = 1

    ###OP LEGAL
    int_op = df[df["Operational Risk - LEGAL"].str.contains(r"Intellectual Property").fillna(False)].index.tolist()
    for rater in int_op:
        grid[5,rater] = 1
    brand_op = df[df["Operational Risk - LEGAL"].str.contains(r"Brand Protection and Reputation").fillna(False)].index.tolist()
    for rater in brand_op:
        grid[6,rater] = 1
    laws_op = df[df["Operational Risk - LEGAL"].str.contains(r"Legal Lawsuit").fillna(False)].index.tolist()
    for rater in laws_op:
        grid[7,rater] = 1

    ###OP
    ineff_op = df[df["Operational Risk"].str.contains(r"Inefficient process").fillna(False)].index.tolist()
    for rater in ineff_op:
        grid[8,rater] = 1
    ineffec_op = df[df["Operational Risk"].str.contains(r"Ineffective process").fillna(False)].index.tolist()
    for rater in ineffec_op:
        grid[9,rater] = 1
    kpi_op = df[df["Operational Risk"].str.contains(r"KPIs are not capturing relevant indicators").fillna(False)].index.tolist()
    for rater in kpi_op:
        grid[10,rater] = 1

    ###COMPL
    country_compl = df[df["Compliance Risks"].str.contains(r"Ability to sell product/service in specific countries").fillna(False)].index.tolist()
    for rater in country_compl:
        grid[11,rater] = 1
    safety_compl = df[df["Compliance Risks"].str.contains(r"Health and safety compliance").fillna(False)].index.tolist()
    for rater in safety_compl:
        grid[12,rater] = 1
    esd_compl = df[df["Compliance Risks"].str.contains(r"ESD Compliance").fillna(False)].index.tolist()
    for rater in esd_compl:
        grid[13,rater] = 1
    limit_compl = df[df["Compliance Risks"].str.contains(r"Product/Service limitations").fillna(False)].index.tolist()
    for rater in limit_compl:
        grid[14,rater] = 1
    stand_compl = df[df["Compliance Risks"].str.contains(r"Compliance with International standard").fillna(False)].index.tolist()
    for rater in stand_compl:
        grid[15,rater] = 1

    ###TEC
    test_tec = df[df["Technical Risks"].str.contains(r"Testability").fillna(False)].index.tolist()
    for rater in test_tec:
        grid[16,rater] = 1
    perf_tec = df[df["Technical Risks"].str.contains(r"Performance").fillna(False)].index.tolist()
    for rater in perf_tec:
        grid[17,rater] = 1
    rel_tec = df[df["Technical Risks"].str.contains(r"Reliability").fillna(False)].index.tolist()
    for rater in rel_tec:
        grid[18,rater] = 1
    av_tec = df[df["Technical Risks"].str.contains(r"Availability").fillna(False)].index.tolist()
    for rater in av_tec:
        grid[19,rater] = 1
    scal_tec = df[df["Technical Risks"].str.contains(r"Scalability").fillna(False)].index.tolist()
    for rater in scal_tec:
        grid[20,rater] = 1
    sec_tec = df[df["Technical Risks"].str.contains(r"Security").fillna(False)].index.tolist()
    for rater in sec_tec:
        grid[21,rater] = 1
    maint_tec = df[df["Technical Risks"].str.contains(r"Maintainability").fillna(False)].index.tolist()
    for rater in maint_tec:
        grid[22,rater] = 1

    ###PROFILE
    const_prof = df[df["What is the profile cost of the risk?"].str.contains(r"Constant").fillna(False)].index.tolist()
    for rater in const_prof:
        grid[23,rater] = 1
    log_prof = df[df["What is the profile cost of the risk?"].str.contains(r"Logarithmic").fillna(False)].index.tolist()
    for rater in log_prof:
        grid[24,rater] = 1
    lin_prof = df[df["What is the profile cost of the risk?"].str.contains(r"Linear").fillna(False)].index.tolist()
    for rater in lin_prof:
        grid[25,rater] = 1
    exp_prof = df[df["What is the profile cost of the risk?"].str.contains(r"Exponential").fillna(False)].index.tolist()
    for rater in exp_prof:
        grid[26,rater] = 1

    ###PROBABILITY
    rare_prob = df[df["Risk Assessment - Probability"].str.contains(r"RARE").fillna(False)].index.tolist()
    for rater in rare_prob:
        grid[27,rater] = 1
    poss_prob = df[df["Risk Assessment - Probability"].str.contains(r"POSSIBLE").fillna(False)].index.tolist()
    for rater in poss_prob:
        grid[28,rater] = 1
    prob_prob = df[df["Risk Assessment - Probability"].str.contains(r"PROBABLE").fillna(False)].index.tolist()
    for rater in prob_prob:
        grid[29,rater] = 1

    ###IMPACT
    low_imp= df[df["Risk Assessment - Impact"].str.contains(r"LOW").fillna(False)].index.tolist()
    for rater in low_imp:
        grid[30,rater] = 1
    med_imp= df[df["Risk Assessment - Impact"].str.contains(r"MEDIUM").fillna(False)].index.tolist()
    for rater in med_imp:
        grid[31,rater] = 1
    hi_imp= df[df["Risk Assessment - Impact"].str.contains(r"HIGH").fillna(False)].index.tolist()
    for rater in hi_imp:
        grid[32,rater] = 1

    print(grid)
    np.savetxt("Temporary.csv", grid, delimiter=',', fmt= "%d")


    #######################       #######################
    ####################### KAPPA #######################
    #######################       #######################

    # DATO UN input_file_name CHE RAPPRESENTA UN FINDING
    # CREA UN DATAFRAME PER CIASCUN BLOCCO DI CATEGORIE
    # (tante righe quante le categorie, tante colonne quanti gli esperti)
    # RITORNA UNA LISTA DI DATAFRAME

    block_names = ["Strategic Risk",
                   "Operational Risk Legal",
                   "Operational Risk",
                   "Compliance Risk",
                   "Technical Risk"
                   # qui sotto da commentare se si trattano separatamente le single-choice
        , "Cost Profile",
                   "Risk Probability",
                   "Risk Impact"
                   ]


    def crea_lista_dei_blocchi(input_file_name):
        df = pd.read_csv(input_file_name)

        # ----------------------------------- Scelta multipla

        # Crea il primo blocco, qui "Strategic_Risk"

        ####CHANGED: k_1 RIDOTTO DI 1 PER NON CONSIDERARE GLI OTHER
        k_1 = 4;  # numero elementi del blocco (numero totale di opzioni)
        start_row = 0
        over_the_top_row = start_row + k_1
        df_block_1 = pd.DataFrame(columns=df.columns, data=df.iloc[range(start_row, over_the_top_row), :])

        ####CHANGED: k_2 RIDOTTO DI 1 PER NON CONSIDERARE GLI OTHER
        # Crea il secondo blocco, qui "Operational_Risk_Legal"
        k_2 = 3;  # numero elementi del blocco (numero totale di opzioni)
        start_row = over_the_top_row
        over_the_top_row = start_row + k_2
        df_block_2 = pd.DataFrame(columns=df.columns, data=df.iloc[range(start_row, over_the_top_row), :])

        ####CHANGED: k_3 RIDOTTO DI 1 PER NON CONSIDERARE GLI OTHER
        # Crea il terzo blocco, qui "Operational_Risk"
        k_3 = 3;  # numero elementi del blocco (numero totale di opzioni)
        start_row = over_the_top_row
        over_the_top_row = start_row + k_3
        df_block_3 = pd.DataFrame(columns=df.columns, data=df.iloc[range(start_row, over_the_top_row), :])

        ####CHANGED: k_4 RIDOTTO DI 1 PER NON CONSIDERARE GLI OTHER
        # Crea il quarto blocco, qui "Compliance_Risk"
        k_4 = 5;  # numero elementi del blocco (numero totale di opzioni)
        start_row = over_the_top_row
        over_the_top_row = start_row + k_4
        df_block_4 = pd.DataFrame(columns=df.columns, data=df.iloc[range(start_row, over_the_top_row), :])

        ####CHANGED: k_5 RIDOTTO DI 1 PER NON CONSIDERARE GLI OTHER
        # Crea il Quinto blocco, qui "Technical_Risk"
        k_5 = 7;  # numero elementi del blocco (numero totale di opzioni)
        start_row = over_the_top_row
        over_the_top_row = start_row + k_5
        df_block_5 = pd.DataFrame(columns=df.columns, data=df.iloc[range(start_row, over_the_top_row), :])

        # ----------------------------------- Scelta singola

        # Crea il Sesto blocco, qui "Cost_Profile"
        k_6 = 4;  # numero elementi del blocco (numero totale di opzioni)
        start_row = over_the_top_row
        over_the_top_row = start_row + k_6
        df_block_6 = pd.DataFrame(columns=df.columns, data=df.iloc[range(start_row, over_the_top_row), :])

        # Crea il Settimo blocco, qui "Risk_Probability"
        k_7 = 3;  # numero elementi del blocco (numero totale di opzioni)
        start_row = over_the_top_row
        over_the_top_row = start_row + k_7
        df_block_7 = pd.DataFrame(columns=df.columns, data=df.iloc[range(start_row, over_the_top_row), :])

        # Crea l'Ottavo blocco, qui "Risk_Impact"
        k_8 = 3;  # numero elementi del blocco (numero totale di opzioni)
        start_row = over_the_top_row
        over_the_top_row = start_row + k_8
        df_block_8 = pd.DataFrame(columns=df.columns, data=df.iloc[range(start_row, over_the_top_row), :])

        df_blocks = []
        df_blocks.append(df_block_1)
        df_blocks.append(df_block_2)
        df_blocks.append(df_block_3)
        df_blocks.append(df_block_4)
        df_blocks.append(df_block_5)
        # qui sotto da commentare se si trattano separatamente le single-choice
        df_blocks.append(df_block_6)
        df_blocks.append(df_block_7)
        df_blocks.append(df_block_8)

        return df_blocks


    def calcola_KAPPA_NEW(single_expert_data):  # "single" perché ciascuna colonna rappresenta un esperto, NON una coppia
        nexperts = single_expert_data.shape[1]  # numero degli esperti, nel paper è chiamato n
        npairs = nexperts * (nexperts - 1) * 0.5  # numero delle coppie, nel paper è chiamato \nu
        k = single_expert_data.shape[0]  # numero totale delle opzioni disponibili, nel paper è chiamato k

        aa = single_expert_data.sum()  # array con il conteggio a_i del numero di opzioni scelte da ciascun esperto

        mydf = single_expert_data

        # ORDINAMENTO! ############################################################à

        # print("\nmydf")
        # print(mydf)

        # aggiungo una nuova riga con il conteggio a_i del numero di opzioni scelte da ciascun esperto:
        # mi serve poi per ordinare le colonne cioè gli esperti in ordine non decrescente di opzioni espresse: a_i <= a_{i+1}
        to_append = pd.Series(aa, index=mydf.columns)
        mydf = mydf.append(to_append, ignore_index=True)

        # cambio i nomi delle colonne per comodità di stampa
        alphabet_list = list(
            string.ascii_uppercase)  # con questa convenzione, massimo n=26 colonne (esperti); TODO: rendere lista più generale
        mycolumns = alphabet_list[:nexperts]
        mydf.columns = mycolumns
        # print("\nmydf+aa")
        # print(mydf)

        # sort dataframe based on last row
        mydf = mydf[mydf.iloc[-1].sort_values(ascending=True).index]
        # print("\nmydf+aa sorted by aa")
        # print(mydf)

        aa_sorted = mydf.iloc[-1]  # memorizza la riga delle somme riordinata

        # un passaggio per creare un dataframe usato dopo
        mydf_SPECIAL = mydf[
            mydf.columns[mydf.iloc[-1] > 0]]  # dataframe privato delle colonne con 0 conteggi, da usare dopo

        # ora rimuove l'ultima riga dal data frame
        mydf.drop([k], axis=0, inplace=True)
        # print("\nmydf+aa sorted by aa, with aa removed")
        # print(mydf)
        # print("---\n")

        # SUM AND RATIO ############################################################################################

        # Qui CALCOLA LE QUANTITA' RILEVANTI per kappa_sum_and_ratio e per kappa_star
        # quelle per kappa_ratio_average che non sono definite per colonne con zero scelte
        # vengono calcolate più sotto usando il dataframe mydf_SPECIAL in cui le colonne vuote sono rimosse

        # SOMMA DEGLI x_ij
        # SOMMA DEI PRODOTTI a_i a_j
        x = 0  # poteva chiamarsi sum_x_ij
        sum_a_i_times_a_j = 0  # nel papiro fino alla versione 11 è chiamato C
        count = 0
        for iexpert in range(0, nexperts - 1):
            for jexpert in range(iexpert + 1, nexperts):
                #            print("%d-%d\n" % (iexpert+1,jexpert+1))
                count = count + 1  # per debug

                # scorre lungo le due colonne
                x_ij = 0
                for index_row, row in mydf.iterrows():  # somma sulle opzioni perché siamo in multi-choice
                    addendo = row.iloc[iexpert] * row.iloc[jexpert]  # addendo=1 if positive agreement
                    x_ij = x_ij + addendo
                # continue

                x = x + x_ij
                sum_a_i_times_a_j = sum_a_i_times_a_j + aa_sorted[iexpert] * aa_sorted[jexpert]

            # continue
        # continue

        print("npairs %d\n" % count)  # per debug

        # SOMMA degli a_i, serve poi per kappa_star
        sum_a_i = 0  # nel paper è chiamato S
        for iexpert in range(0, nexperts):
            sum_a_i = sum_a_i + aa_sorted[iexpert]

        # reference per sum and ratio
        # anche nel paper è chiamato D
        D = nexperts * (nexperts - 1) * 0.5 * aa_sorted[0]  # questo sarebbe il primo termine (n(n-1)/2) * a_1
        for jexpert in range(1, nexperts - 1):  # si parte dal secondo esperto (indice j=2, quindi jexpert = 1),
            # perché il primo è già contato sopra
            # e non si considera l'ultimo (indice n-1) perché non fa coppie
            j = jexpert + 1  # per allinearsi alla NOTAZIONE dell'articolo per il calcolo del coefficiente
            D = D + (nexperts - j + 1) * (nexperts - j) * (
                    aa_sorted[jexpert] - aa_sorted[jexpert - 1]) / 2  # ma lascio jexpert perché gli indici sono ok
        #        D=D+(nexperts-j+1)*(nexperts-j)*(aa_sorted[j]-aa_sorted[j-1])/2 # questo infatti da risultati insensati
        # continue

        C = sum_a_i_times_a_j
        S = sum_a_i

        # KAPPA_sr

        num = (x * k - C)
        den = (k * D - C)

        if den > 0:
            kappa_sum_and_ratio = num / den
        else:
            kappa_sum_and_ratio = np.nan

            # KAPPA STAR

        den = k * S * (nexperts - 1) * 0.5 - C

        if den > 0:
            kappa_star = num / den
        else:
            kappa_star = np.nan

            # RATIOS AVERAGE ############################################################################################

        # Qui CALCOLA LE QUANTITA' RILEVANTI per kappa_ratios_average
        # le colonne con zero scelte sono rimosse, si assume cioè che l'esperto non si sia voluto esprimere

        # il dataframe privato mydf_SPECIAL delle colonne con zero conteggi è stato creato più sopra,
        # prima di eliminare la riga dei conteggi

        # si contano gli esperti e le coppie
        nexperts = mydf_SPECIAL.shape[
            1]  # numero degli esperti che hanno espresso almeno una scelta, nel paper è chiamato n
        npairs = nexperts * (nexperts - 1) * 0.5  # numero delle coppie, nel paper è chiamato \nu

        if npairs < 1:  #######################################################################
            print("npairs<1, k_ra=nan")
            kappa_ratio_average = np.nan
        else:  #######################################################################
            # print("mydf_SPECIAL+aa")
            # print(mydf_SPECIAL)

            aa_sorted = mydf_SPECIAL.iloc[-1]  # memorizza la riga delle somme riordinata

            # rimuove l'ultima riga dal data frame
            mydf_SPECIAL.drop([k], axis=0, inplace=True)

            # \pi ratio-average OSSERVATO

            # SOMMA DEGLI x_ij con divisione per a_i
            sum_x_ij_over_a_i = 0
            count = 0
            for iexpert in range(0, nexperts - 1):
                for jexpert in range(iexpert + 1, nexperts):
                    #            print("%d-%d\n" % (iexpert+1,jexpert+1))
                    count = count + 1  # per debug
                    # scorre lungo le due colonne
                    x_ij = 0
                    for index_row, row in mydf_SPECIAL.iterrows():
                        addendo = row.iloc[iexpert] * row.iloc[jexpert]  # addendo=1 if positive agreement
                        x_ij = x_ij + addendo
                    # continue
                    sum_x_ij_over_a_i = sum_x_ij_over_a_i + x_ij / aa_sorted[iexpert]
                # continue
            # continue
            print("npairs %d\n" % count)  # per debug
            pi_observed = sum_x_ij_over_a_i / npairs

            # \pi ratio-average ATTESO

            # sum_{j=2}^n (j-1)a_j
            sum_a_j_times_occurrences = 0  # nel paper fino alla versione 11 si chiama B
            for jexpert in range(1, nexperts):  # si parte dal secondo esperto (indice j=2, quindi jexpert = 1)
                j = jexpert + 1  # per allinearsi alla notazione dell'articolo
                sum_a_j_times_occurrences = sum_a_j_times_occurrences + (j - 1) * aa_sorted[jexpert]
            # continue
            pi_expected = sum_a_j_times_occurrences / (npairs * k)

            num = (pi_observed - pi_expected)
            den = (1 - pi_expected)
            print(num)
            print(den)
            if den > 0:
                kappa_ratio_average = num / den
            else:
                kappa_ratio_average = np.nan
                # endif #######################################################################

        return kappa_ratio_average, kappa_sum_and_ratio, kappa_star


    # QUESTO E' IL DRIVER PER IL CALCOLO VERO E PROPRIO

    name_of_first_column = 'Categories'
    # righe prima colonna
    tmp = pd.DataFrame({name_of_first_column: block_names})  # tutte le colonne
    tmp_0 = pd.DataFrame({name_of_first_column: block_names})  # solo kappa r.a
    tmp_1 = pd.DataFrame({name_of_first_column: block_names})  # solo kappa s.r.
    tmp_2 = pd.DataFrame({name_of_first_column: block_names})  # solo kappa*
    # input_file_numbers=["01","02","03","04","05","06","07","08","09","10"]
    # prefix=".\\Finding"
    input_file_numbers = ["09"]
    # prefix=".\\FindingTENINDIA"
    for s in input_file_numbers:
        input_file_name = r"Temporary.csv"
        #output_file_name = "output_NEW.csv"
        print("Elaborazione di %s\n" % input_file_name)
        df_blocks = crea_lista_dei_blocchi(input_file_name)
        #output = pd.DataFrame(columns=[s + " $\kappa_{ra}$ ", s + " $\kappa_{sr}$ ", s + " $\kappa^*$ "])
        #output_0 = pd.DataFrame(columns=[s + " $\kappa_{ra}$ "])
        #output_1 = pd.DataFrame(columns=[s + " $\kappa_{sr}$ "])
        #output_2 = pd.DataFrame(columns=[s + " $\kappa^*$ "])
        idx_block = 0

        ########ADDED CODE#########
        k_raList = []
        k_srList = []
        k_ndList = []
        ##############END ADDED CODE############

        for block in df_blocks:
            print("\nProcessing block: %s" % block_names[idx_block])
            idx_block = idx_block + 1
            myrow = calcola_KAPPA_NEW(block)  ############################# THIS IS IT
            #to_append = pd.Series(myrow, index=output.columns)
            #output = output.append(to_append, ignore_index=True)
            #
            myrow_0 = myrow[0]
            k_raList.append(myrow_0)  #######ADDED LINE########
            #to_append_0 = pd.Series(myrow_0, index=output_0.columns)
            #output_0 = output_0.append(to_append_0, ignore_index=True)
            #
            myrow_1 = myrow[1]
            #to_append_1 = pd.Series(myrow_1, index=output_1.columns)
            k_srList.append(myrow_1)  #######ADDED LINE########
            #output_1 = output_1.append(to_append_1, ignore_index=True)
            #
            myrow_2 = myrow[2]
            #to_append_2 = pd.Series(myrow_2, index=output_2.columns)
            k_ndList.append(myrow_2)  #######ADDED LINE########
            #output_2 = output_2.append(to_append_2, ignore_index=True)
            #
        ###THIS SAVES RESULT ON CSV###
        #output.to_csv(output_file_name, encoding='utf-8', index=False)
        #tmp = tmp.join(output)
        #tmp_0 = tmp_0.join(output_0)
        #tmp_1 = tmp_1.join(output_1)
        #tmp_2 = tmp_2.join(output_2)

        import Grafica as graf
        graf.buildtable2(file_handler2, app2, k_raList, k_srList, k_ndList)