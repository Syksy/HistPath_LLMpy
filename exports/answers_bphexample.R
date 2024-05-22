answers <- read.table("answers.tsv", header=TRUE, sep="\t")

negatives <- c(NA, "Ei", "ei", "No", "no", "False", "false")
positives <- c("Kyllä", "kyllä", "Yes", "yes", "True", "true")
# Correct answers for whether the statement should've been classified as BPH
bphs <- list(
	negatives, # inputIndex 0
	negatives, # 1
	negatives, # 2
	negatives, # 3
	negatives, # 4
	negatives, # 5
	negatives, # 6
	negatives, # 7
	positives, # 8
	negatives, # 9
	negatives, # 10
	negatives, # 11
	negatives, # 12
	negatives, # 13
	negatives, # 14
	negatives, # 15
	negatives, # 16
	negatives, # 17
	negatives, # 18
	positives, # 19
	negatives, # 20
	positives, # 21
	negatives, # 22
	negatives, # 23
	negatives, # 24
	negatives, # 25
	positives, # 26
	negatives, # 27
	negatives, # 28
	negatives  # 29	
)

bphdat <- expand.grid(
	model = c("gpt-3.5-turbo", "gpt-4-turbo", "gemini-1.0-pro-001", "meta/meta-llama-3-70b-instruct"),
	promptIndex = 0:19,
	correctness = NA_real_
)

for(i in 1:nrow(bphdat)){
	w <- which(answers$model == bphdat[i,"model"] & answers$promptIndex == bphdat[i,"promptIndex"])
	correct <- 0
	ans <- answers[w,"answer"]
	# Iterate across 30 Finnish statements
	for(index in 1:30){
		if(ans[index] %in% bphs[[index]]){
			correct <- correct + 1
		}
	}
	bphdat[i,"correctness"] <- round(correct/30, 2) # Two decimal precision
}

models <- c("gpt-3.5-turbo", "gpt-4-turbo", "gemini-1.0-pro-001", "meta/meta-llama-3-70b-instruct")

par(las=1, mar=c(4,6,1,1))
plot.new()
plot.window(xlim=extendrange(0:19), ylim=c(0,1))
axis(1, at=0:19); axis(2, at=seq(0,1,by=.1)); box()
abline(v=0:19, col="grey")
abline(h=seq(0,1,by=.1), col="grey")
for(modelIndex in 1:length(models)){
	bphsub <- bphdat[which(bphdat$model == models[modelIndex]),"correctness"]
	points(0:19, bphsub, col=modelIndex, pch=16)
	points(0:19, bphsub, col=modelIndex, pch=16, type="l", lwd=2.5)
}
legend("topleft", legend=models, pch=16, lwd=2.5, col=1:4, bg="white")
title(xlab="Prompt index", ylab="Proportion of correctly \nassigned a benign labels")



# False positives from the gibberish are anything that deviate from NAs

fps <- expand.grid(
	model = models,
	promptIndex = 0:19,
	fpr = NA_real_ # False positive rate
)

for(i in 1:nrow(fps)){
	w <- which(answers$model == fps[i,"model"] & answers$promptIndex == fps[i,"promptIndex"])
	fps[i,"fpr"] <- sum(!is.na(answers[w,"answer"]))/length(w)
}
	
par(las=1, mar=c(4,6,1,1))
plot.new()
plot.window(xlim=extendrange(0:19), ylim=c(0,1))
axis(1, at=0:19); axis(2, at=seq(0,1,by=.1)); box()
abline(v=0:19, col="grey")
abline(h=seq(0,1,by=.1), col="grey")
for(modelIndex in 1:length(models)){
	fpssub <- fps[which(fps$model == models[modelIndex]),"fpr"]
	points(0:19, fpssub, col=modelIndex, pch=16)
	points(0:19, fpssub, col=modelIndex, pch=16, type="l", lwd=2.5)
}
legend("bottomleft", legend=models, pch=16, lwd=2.5, col=1:4, bg="white")
title(xlab="Prompt index", ylab="Proportion of non-NA answers\n across all questions when fed gibberish")


