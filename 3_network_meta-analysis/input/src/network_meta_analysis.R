
network_meta_analysis <- function(df, sm = "", reference = "") {

    data_path <- paste0(root, "/input/data/sheets_for_analysis/", df, ".csv")
    data <- read.csv(data_path)


    m.netmeta <- netmeta(
        data = data,
        studlab = study,
        TE = TE,
        treat1 = treat1,
        treat2 = treat2,
        seTE = seTE,
        sm = paste0(sm),
        reference.group = paste0(reference),
        random = TRUE,
        common = FALSE,
        )

    sink(file = paste0("./output/results/netmeta/", df, ".txt"))
    print(m.netmeta)
    sink()

    sink(file = paste0("./output/results/netsplit/", df, ".txt"))
    netsplit <- netsplit(m.netmeta)
    print(netsplit)
    sink()

    order =  c("BPTB", "HT", "QT", "PLT", "AT", "TA")
    seq = order[order %in% m.netmeta$trts]

    netleague <- netleague(m.netmeta,
                           bracket = "[",
                           digits = 3,
                           details = TRUE,
                           seq = seq
                           )
    write.csv(netleague$random, paste0("./output/results/netleague/", df, ".csv"))

}
