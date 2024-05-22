dat <- read.table("disconcordant.tsv", header=TRUE)

# Prompt designs in Finnish
fin_prompts = c(0, 1, 2, 4:16)
# Prompt designs in English
eng_prompts = c(3, 17:19)

cols <- rep("blue", times=20)
cols[eng_prompts+1] <- "red"

pdf("disconcordant.pdf", width=10, height=3)
par(mfrow=c(1,4), las=1)
for(model in c("gpt-3.5-turbo", "gpt-4-turbo", "gemini-1.0-pro-001", "meta/meta-llama-3-70b-instruct")){
	plot.new()
	plot.window(xlim=extendrange(0:19), ylim=c(0,1))
	abline(v=0:19, col="grey")
	abline(h=seq(0,1,by=.1), col="grey")
	points(0:19, dat[which(dat$model == model),"disconcordant"]/70, col=cols, pch=16)
	title(main=model, xlab="Prompt index", ylab="Proportion disconcordant triplicates")
	axis(1, at=0:19); axis(2, at=seq(0,1,by=.1)); box()
}
legend("topright", pch=16, col=c("blue", "red"), legend=c("Prompt in Finnish", "Prompt in English"), bg="white")
dev.off()



