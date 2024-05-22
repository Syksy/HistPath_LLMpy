# Read the answers tabulated
answers <- read.table("answers.tsv", header=TRUE, sep="\t", row.names=1)
# Use ComplexHeatmaps to nicely present the results
library(ComplexHeatmap)

# models (gpt 3.5, 4, gemini, and llama-3)
modelnames <- unique(answers$model)

# Create lists of lists with matrices as elements
ll <- list()

# Interate across models
for(model in modelnames){
	# Add a new list for 
	ll[[length(ll)+1]] <- list()
	# Iterate across the questions
	for(questionIndex in 0:5){
		# Create {-1,0,1} correctness matrix (with -2 as JSON parse error)	
		#m <- matrix(-2, nrow=length(0:19), ncol=length(0:69))
		# Only include correct language (e.g. machine translated English statement inputs for English prompts)
		m <- matrix(-2, nrow=length(0:19), ncol=length(0:39))
		# Iterate over rows (prompt designs) and cols (input statements)
		for(i in 0:(nrow(m)-1)){
			for(j in 0:(ncol(m)-1)){
				# Prompts designed in English will take the machine-translated English statements
				# Prompts with index 3, 17, 18, and 19 were in English
				offset <- ifelse(i %in% c(3, 17, 18, 19), 0, 30)
				w <- which(
					(answers$model == model) & 
					(answers$promptIndex == i) &
					(answers$inputIndex == j + offset) & 
					(answers$answerIndex == questionIndex)
				)
				if(length(w)>0){
					m[i+1,j+1] <- answers[w,"correct"]
				}
			}
		}
		rownames(m) <- paste0("promptIndex_", 0:19)
		#colnames(m) <- paste0("inputIndex_", 0:69)
		colnames(m) <- paste0("inputIndex_", 0:39)
		ll[[length(ll)]][[length(ll[[length(ll)]])+1]] <- m
	}
	names(ll[[length(ll)]]) <- paste0("questionIndex_", 0:5)
}
names(ll) <- modelnames

# Element annotations for heatmaps
annots <- c("-2" = "Parse fail", "-1" = "Wrong", "0" = "Ambiguous", "1" = "Correct")
# Element colourings
cols = c("-2" = "darkred", "-1" = "orange", "0" = "white", "1" = "cyan")
# Iterate through heatmaps, and horizontally group together those from same question
htlists <- list()
for(questionIndex in 0:5){
	m <- ll[[1]][[questionIndex+1]]
	topanno <- apply(m, MARGIN=2, FUN=\(x){ matrix(nc=4, c(sum(x==-2)/length(x), sum(x==-1)/length(x), sum(x==0)/length(x), sum(x==1)/length(x)) ) })
	ta <- ComplexHeatmap::HeatmapAnnotation("." = anno_barplot(t(topanno), height=unit(2, "cm"), gp=gpar(fill=c("darkred", "orange", "white", "cyan"), border=NA, lty="blank")))
	leftanno <- apply(m, MARGIN=1, FUN=\(x){ matrix(nc=4, c(sum(x==-2)/length(x), sum(x==-1)/length(x), sum(x==0)/length(x), sum(x==1)/length(x)) ) })
	la <- ComplexHeatmap::rowAnnotation("." = anno_barplot(t(leftanno), height=unit(2, "cm"), gp=gpar(fill=c("darkred", "orange", "white", "cyan"), border=NA, lty="blank")))
	
	htlists[[length(htlists)+1]] <- ComplexHeatmap::Heatmap(m, cluster_rows = FALSE, cluster_columns = FALSE, col = cols, top_annotation = ta, left_annotation = la, show_row_names = FALSE, show_column_names = FALSE, show_heatmap_legend = FALSE)
	
	for(modelIndex in 2:length(modelnames)){
		m <- ll[[modelIndex]][[questionIndex+1]]
		topanno <- apply(m, MARGIN=2, FUN=\(x){ matrix(nc=4, c(sum(x==-2)/length(x), sum(x==-1)/length(x), sum(x==0)/length(x), sum(x==1)/length(x)) ) })
		ta <- ComplexHeatmap::HeatmapAnnotation("." = anno_barplot(t(topanno), height=unit(2, "cm"), gp=gpar(fill=c("darkred", "orange", "white", "cyan"), border=NA, lty="blank")))
		leftanno <- apply(m, MARGIN=1, FUN=\(x){ matrix(nc=4, c(sum(x==-2)/length(x), sum(x==-1)/length(x), sum(x==0)/length(x), sum(x==1)/length(x)) ) })
		la <- ComplexHeatmap::rowAnnotation("." = anno_barplot(t(leftanno), height=unit(2, "cm"), gp=gpar(fill=c("darkred", "orange", "white", "cyan"), border=NA, lty="blank")))

		htlists[[length(htlists)]] <- htlists[[length(htlists)]] + ComplexHeatmap::Heatmap(m, cluster_rows = FALSE, cluster_columns = FALSE, col = cols, top_annotation = ta, left_annotation = la, show_row_names = FALSE, show_column_names = FALSE, show_heatmap_legend = FALSE)
		
	}
}

# Output each question as its own PDF

pdf("Outputs_q0.pdf", width=20, height=6)
htlists[[1]]
dev.off()

pdf("Outputs_q1.pdf", width=20, height=6)
htlists[[2]]
dev.off()

pdf("Outputs_q2.pdf", width=20, height=6)
htlists[[3]]
dev.off()

pdf("Outputs_q3.pdf", width=20, height=6)
htlists[[4]]
dev.off()

pdf("Outputs_q4.pdf", width=20, height=6)
htlists[[5]]
dev.off()

pdf("Outputs_q5.pdf", width=20, height=6)
htlists[[6]]
dev.off()



